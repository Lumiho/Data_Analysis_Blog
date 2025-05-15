import type { NextConfig } from 'next'
import withMDX from '@next/mdx' // you'll need to install this

const nextConfig: NextConfig = {
  reactStrictMode: true,
  experimental: {
    // @ts-expect-error: serverActions is experimental and not typed yet
    serverActions: true,
  },
}

export default withMDX({
  extension: /\.mdx?$/,
  options: {
    remarkPlugins: [],
    rehypePlugins: [],
  },
})(nextConfig)
