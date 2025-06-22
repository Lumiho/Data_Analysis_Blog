'use client'

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

interface PostsClientProps {
  posts: Post[]
  allTags: string[]
}

export default function PostsClient({ posts, allTags }: PostsClientProps) {
  const [selectedTags, setSelectedTags] = useState<string[]>([])

  const handleTagClick = (tag: string) => {
    setSelectedTags(prev => 
      prev.includes(tag) 
        ? prev.filter(t => t !== tag)
        : [...prev, tag]
    )
  }

  const filteredPosts = selectedTags.length > 0 
    ? posts.filter(post => 
        post.tags && selectedTags.some(tag => post.tags!.includes(tag))
      )
    : []

  const otherPosts = selectedTags.length > 0 
    ? posts.filter(post => 
        !post.tags || !selectedTags.some(tag => post.tags!.includes(tag))
      )
    : []

  const PostCard = ({ post }: { post: Post }) => (
    <article className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg overflow-hidden border border-gray-200 dark:border-gray-700 hover:border-[#B8860B] dark:hover:border-[#B8860B] transition-colors">
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
  )

  return (
    <>
      {/* Tags Filter */}
      <div className="mb-8">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
          Filter by Topic
        </h2>
        <div className="flex flex-wrap gap-2">
          {allTags.map(tag => (
            <button
              key={tag}
              onClick={() => handleTagClick(tag)}
              className={`px-4 py-2 rounded-full text-sm transition-colors ${
                selectedTags.includes(tag)
                  ? 'bg-[#B8860B] text-white'
                  : 'bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-[#B8860B]/10 dark:hover:bg-[#B8860B]/20'
              }`}
            >
              {tag}
            </button>
          ))}
        </div>
      </div>

      {/* Filtered Posts Section */}
      {selectedTags.length > 0 && filteredPosts.length > 0 && (
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Posts with tags: {selectedTags.join(', ')}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {filteredPosts.map(post => (
              <PostCard key={post.slug} post={post} />
            ))}
          </div>
        </div>
      )}

      {/* Divider */}
      {selectedTags.length > 0 && filteredPosts.length > 0 && otherPosts.length > 0 && (
        <div className="my-12">
          <div className="border-t border-gray-300 dark:border-gray-600"></div>
        </div>
      )}

      {/* Other Posts Section */}
      {selectedTags.length > 0 && otherPosts.length > 0 && (
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Other Posts
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {otherPosts.map(post => (
              <PostCard key={post.slug} post={post} />
            ))}
          </div>
        </div>
      )}

      {/* All Posts (when no tags selected) */}
      {selectedTags.length === 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {posts.map(post => (
            <PostCard key={post.slug} post={post} />
          ))}
        </div>
      )}

      {/* No results message */}
      {selectedTags.length > 0 && filteredPosts.length === 0 && (
        <div className="text-center py-12">
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
            No posts found with the selected tags
          </h3>
          <p className="text-gray-600 dark:text-gray-400">
            Try selecting different tags or clear the filter to see all posts.
          </p>
          <button
            onClick={() => setSelectedTags([])}
            className="mt-4 px-6 py-2 bg-[#B8860B] text-white rounded-lg hover:bg-[#B8860B]/90 transition-colors"
          >
            Clear Filter
          </button>
        </div>
      )}
    </>
  )
} 