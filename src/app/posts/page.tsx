import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import PostsClient from './PostsClient'

interface Post {
  slug: string
  title: string
  date: string
  summary: string
  author?: string
  readingTime?: string
  tags?: string[]
  draft?: boolean
}

async function getPosts(): Promise<Post[]> {
  const postsDirectory = path.join(process.cwd(), 'src', 'posts')
  const filenames = fs.readdirSync(postsDirectory)

  const allPosts = filenames
    .filter(filename => filename.endsWith('.mdx'))
    .map(filename => {
      const filePath = path.join(postsDirectory, filename)
      const fileContent = fs.readFileSync(filePath, 'utf8')
      const { data } = matter(fileContent)
      
      const post = {
        slug: filename.replace('.mdx', ''),
        title: data.title,
        date: data.date,
        summary: data.summary,
        author: data.author,
        readingTime: data.readingTime,
        tags: data.tags,
        draft: data.draft,
      }
      
      // Debug each post
      console.log(`Processing ${filename}:`, { 
        slug: post.slug, 
        draft: post.draft, 
        draftType: typeof post.draft,
        title: post.title 
      })
      
      return post
    })

  // Debug logging
  console.log('All posts:', allPosts.map(p => ({ slug: p.slug, draft: p.draft, title: p.title })))
  
  const posts = allPosts
    .filter(post => {
      const isDraft = post.draft === true;
      console.log(`Filtering ${post.slug}: draft=${post.draft}, isDraft=${isDraft}`);
      return !isDraft;
    })
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())

  console.log('Filtered posts:', posts.map(p => ({ slug: p.slug, title: p.title })))

  return posts
}

export default async function BlogPage() {
  const posts = await getPosts()
  const allTags = Array.from(new Set(posts.flatMap(post => post.tags || [])))

  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Header */}
      <div className="relative bg-gradient-to-r from-blue-600 to-indigo-700 py-16 px-4">
        <div className="pattern-overlay absolute inset-0 opacity-40"></div>
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <h1 className="text-4xl font-bold text-white mb-4">
            Latest Posts
          </h1>
          <p className="text-xl text-blue-100">
            Discover insights about data analysis, visualization, and more
          </p>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-7xl mx-auto px-4 py-12">
        <PostsClient posts={posts} allTags={allTags} />
      </div>
    </div>
  )
}
