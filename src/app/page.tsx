import Link from 'next/link'
import Image from 'next/image'

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4 py-12 font-[family-name:var(--font-geist-sans)]">
      {/* Navbar */}
      <nav className="w-full max-w-4xl flex justify-between items-center mb-16 border-b pb-4">
        <h1 className="text-xl font-bold text-foreground">Leo’s Data Blog 📊</h1>
        <ul className="flex gap-6 text-sm font-medium">
          <li><Link href="/" className="hover:underline">Home</Link></li>
          <li><Link href="/blog" className="hover:underline">Blog</Link></li>
          <li><Link href="/about" className="hover:underline">About</Link></li>
        </ul>
      </nav>

      {/* Main content */}
      <main className="text-center max-w-xl">
        <Image
          src="/next.svg" 
          alt="Next.js logo"
          width={150}
          height={30}
          className="mx-auto mb-8 dark:invert"
        />
        <h2 className="text-3xl font-semibold mb-4">Welcome to My Data Blog</h2>
        <p className="text-base text-gray-600 dark:text-gray-400">
          I analyze datasets from <strong>Our World in Data</strong> and share insights on health,
          climate, economics, and more.
        </p>
        <div className="mt-8">
          <Link
            href="/blog"
            className="inline-block px-6 py-2 bg-black text-white rounded hover:bg-gray-800 dark:bg-white dark:text-black dark:hover:bg-gray-200 transition"
          >
            Read Blog Posts
          </Link>
        </div>
      </main>
    </div>
  )
}
