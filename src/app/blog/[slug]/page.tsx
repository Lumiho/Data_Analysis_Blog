//dynamic route for pages
import fs from 'fs'
import path from 'path'
import { notFound } from 'next/navigation'

export const dynamicParams = false

// define list of slugs with fs
export async function generateStaticParams() {
    const postsDir = path.join(process.cwd(), 'src', 'posts')
    const filenames = fs.readdirSync(postsDir)
  
    return filenames
      .filter(name => name.endsWith('.mdx'))
      .map(name => ({
        slug: name.replace(/\.mdx$/, ''),
      }))
  }

export default async function BlogPost({ params }: { params: { slug: string } }) {
  try {
    // Import MDX directly as a React component
    const Post = (await import(`../../../../posts/${params.slug}.mdx`)).default

    return (
      <article className="prose dark:prose-invert max-w-screen-md mx-auto py-20">
        <Post />
      </article>
    )
  } catch {
    return notFound()
  }
}
