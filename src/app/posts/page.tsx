import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import { useState } from 'react'

interface Post {
  slug: string
  title: string
  date: string
  summary: string
  author?: string
  readingTime?: string
  tags?: string[]
}

async function getPosts(): Promise<Post[]> {
  const postsDirectory = path.join(process.cwd(), 'src', 'posts')
  const filenames = fs.readdirSync(postsDirectory)

  const posts = filenames
    .filter(filename => filename.endsWith('.mdx'))
    .map(filename => {
      const filePath = path.join(postsDirectory, filename)
      const fileContent = fs.readFileSync(filePath, 'utf8')
      const { data } = matter(fileContent)
      
      return {
        slug: filename.replace('.mdx', ''),
        title: data.title,
        date: data.date,
        summary: data.summary,
        author: data.author,
        readingTime: data.readingTime,
        tags: data.tags,
      }
    })
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())

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
        {/* Tags Filter */}
        <div className="mb-8">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            Filter by Topic
          </h2>
          <div className="flex flex-wrap gap-2">
            {allTags.map(tag => (
              <button
                key={tag}
                className="px-4 py-2 rounded-full text-sm bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-[#B8860B]/10 dark:hover:bg-[#B8860B]/20 transition-colors"
              >
                {tag}
              </button>
            ))}
          </div>
        </div>

        {/* Posts Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {posts.map(post => (
            <article
              key={post.slug}
              className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg overflow-hidden border border-gray-200 dark:border-gray-700 hover:border-[#B8860B] dark:hover:border-[#B8860B] transition-colors"
            >
              <div className="p-6">
                {/* Tags */}
                {post.tags && post.tags.length > 0 && (
                  <div className="flex flex-wrap gap-2 mb-4">
                    {post.tags.map(tag => (
                      <span
                        key={tag}
                        className="px-2 py-1 text-xs bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 rounded-full"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                )}

                {/* Title */}
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                  <a
                    href={`/posts/${post.slug}`}
                    className="hover:text-[#B8860B] dark:hover:text-[#B8860B]"
                  >
                    {post.title}
                  </a>
                </h3>

                {/* Summary */}
                <p className="text-gray-600 dark:text-gray-400 mb-4">
                  {post.summary}
                </p>

                {/* Meta info */}
                <div className="flex items-center text-sm text-gray-500 dark:text-gray-400">
                  {post.author && (
                    <span className="mr-3">{post.author}</span>
                  )}
                  <time dateTime={post.date}>
                    {new Date(post.date).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric'
                    })}
                  </time>
                  {post.readingTime && (
                    <span className="ml-3">{post.readingTime} min read</span>
                  )}
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </div>
  )
}
