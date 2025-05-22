//dynamic route for pages
import fs from 'fs'
import path from 'path'
import { notFound } from 'next/navigation'
import { compileMDX } from 'next-mdx-remote/rsc'

export const dynamicParams = false

interface Frontmatter {
  title: string
  date: string
  summary: string
  author?: string
  readingTime?: string
  tags?: string[]
}

export async function generateStaticParams() {
  const postsDir = path.join(process.cwd(), 'src', 'posts')
  const filenames = fs.readdirSync(postsDir)

  return filenames
    .filter(name => name.endsWith('.mdx'))
    .map(name => ({
      slug: name.replace(/\.mdx$/, ''),
    }))
}

export default async function BlogPost({
  params,
}: Readonly<{
  params: Readonly<{ slug: string }>
}>) {
  const postsDirectory = path.join(process.cwd(), 'src', 'posts')
  const filePath = path.join(postsDirectory, `${params.slug}.mdx`)

  try {
    if (!fs.existsSync(filePath)) {
      return notFound()
    }

    const source = fs.readFileSync(filePath, 'utf8')
    const { content, frontmatter } = await compileMDX<Frontmatter>({
      source,
      options: { parseFrontmatter: true }
    })

    return (
      <main className="min-h-screen bg-white dark:bg-gray-900">
        <article className="max-w-3xl mx-auto px-4 py-12">
          {/* Header Section */}
          <header className="mb-12 text-center">
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              {frontmatter.title}
            </h1>
            
            {/* Meta Information */}
            <div className="flex items-center justify-center space-x-4 text-sm text-gray-600 dark:text-gray-400 mb-6">
              {frontmatter.date && (
                <time dateTime={frontmatter.date}>
                  {new Date(frontmatter.date).toLocaleDateString('en-US', {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                  })}
                </time>
              )}
              {frontmatter.readingTime && (
                <>
                  <span>•</span>
                  <span>{frontmatter.readingTime} min read</span>
                </>
              )}
              {frontmatter.author && (
                <>
                  <span>•</span>
                  <span>By {frontmatter.author}</span>
                </>
              )}
            </div>

            {/* Tags */}
            {frontmatter.tags && frontmatter.tags.length > 0 && (
              <div className="flex flex-wrap justify-center gap-2 mb-8">
                {frontmatter.tags.map((tag) => (
                  <span
                    key={tag}
                    className="px-3 py-1 text-sm bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 rounded-full"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}

            {/* Summary */}
            {frontmatter.summary && (
              <p className="text-lg text-gray-600 dark:text-gray-400 italic">
                {frontmatter.summary}
              </p>
            )}
          </header>

          {/* Content */}
          <div className="prose dark:prose-invert prose-lg max-w-none">
            {content}
          </div>
        </article>
      </main>
    )
  } catch (error) {
    console.error('Error loading post:', error)
    return notFound()
  }
}
