import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Data Analysis Blog",
  description: "Exploring data science, analysis, and modern development practices",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* Navigation */}
        <nav className="sticky top-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm border-b border-gray-200 dark:border-gray-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between items-center h-16">
              {/* Logo */}
              <Link href="/" className="flex items-center space-x-2">
                <span className="text-2xl">📊</span>
                <span className="font-bold text-xl text-gray-900 dark:text-white">
                  Data Blog
                </span>
              </Link>

              {/* Navigation Links */}
              <div className="hidden md:flex items-center space-x-8">
                <Link 
                  href="/" 
                  className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                >
                  Home
                </Link>
                <Link 
                  href="/posts" 
                  className="text-gray-600 dark:text-gray-300 hover:text-[#B8860B] dark:hover:text-[#B8860B] transition-colors"
                >
                  Posts
                </Link>
                <Link 
                  href="/about" 
                  className="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                >
                  About
                </Link>
              </div>

              {/* Mobile Menu Button */}
              <button className="md:hidden p-2 rounded-md text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">
                <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
          </div>
        </nav>

        {children}

        {/* Footer */}
        <footer className="bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800">
          <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {/* Brand */}
              <div>
                <Link href="/" className="flex items-center space-x-2">
                  <span className="text-2xl">📊</span>
                  <span className="font-bold text-xl text-gray-900 dark:text-white">
                    Data Blog
                  </span>
                </Link>
                <p className="mt-4 text-gray-600 dark:text-gray-400">
                  Exploring the world of data science and analysis.
                </p>
              </div>

              {/* Quick Links */}
              <div>
                <h3 className="text-sm font-semibold text-gray-900 dark:text-white uppercase tracking-wider">
                  Quick Links
                </h3>
                <ul className="mt-4 space-y-4">
                  <li>
                    <Link 
                      href="/posts" 
                      className="text-gray-600 dark:text-gray-400 hover:text-[#B8860B] dark:hover:text-[#B8860B] transition-colors"
                    >
                      All Posts
                    </Link>
                  </li>
                  <li>
                    <Link 
                      href="/about" 
                      className="text-gray-600 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
                    >
                      About Me
                    </Link>
                  </li>
                </ul>
              </div>

              {/* Social Links */}
              <div>
                <h3 className="text-sm font-semibold text-gray-900 dark:text-white uppercase tracking-wider">
                  Connect
                </h3>
                <ul className="mt-4 space-y-4">
                  <li>
                    <a 
                      href="https://www.linkedin.com/in/leonardo-zavala-jimenez-651801210"
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="text-gray-600 dark:text-gray-400 hover:text-[#B8860B] dark:hover:text-[#B8860B] transition-colors"
                    >
                      LinkedIn
                    </a>
                  </li>
                  <li>
                    <a 
                      href="https://github.com" 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="text-gray-600 dark:text-gray-400 hover:text-[#B8860B] dark:hover:text-[#B8860B] transition-colors"
                    >
                      GitHub
                    </a>
                  </li>
                  <li>
                    <a 
                      href="mailto:zavalaleo715@yahoo.com"
                      className="text-gray-600 dark:text-gray-400 hover:text-[#B8860B] dark:hover:text-[#B8860B] transition-colors"
                    >
                      zavalaleo715@yahoo.com
                    </a>
                  </li>
                </ul>
              </div>
            </div>

            <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-800">
              <p className="text-center text-gray-500 dark:text-gray-400">
                © {new Date().getFullYear()} Data Blog. All rights reserved.
              </p>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
