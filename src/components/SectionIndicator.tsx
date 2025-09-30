'use client'

import { useEffect, useState } from 'react'

interface Section {
  id: string
  title: string
  element: HTMLElement
}

export default function SectionIndicator() {
  const [currentSection, setCurrentSection] = useState<string>('')

  useEffect(() => {
    const observerOptions = {
      rootMargin: '-20% 0px -70% 0px',
      threshold: 0
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const sectionTitle = entry.target.textContent?.trim() || ''
          setCurrentSection(sectionTitle)
        }
      })
    }, observerOptions)

    // Find all section headers (h2 and h3 elements with section numbers)
    const sectionHeaders = document.querySelectorAll('h2, h3')
    sectionHeaders.forEach((header) => {
      const text = header.textContent?.trim() || ''
      if (text === 'Title' || text.match(/^[IVX]+\./)) {
        observer.observe(header)
      }
    })

    return () => {
      sectionHeaders.forEach((header) => {
        observer.unobserve(header)
      })
    }
  }, [])

  if (!currentSection) return null

  const displayText = currentSection === 'Title' ? 'Introduction' : currentSection

  return (
    <div className="fixed top-20 right-4 z-40 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg shadow-lg px-4 py-2 text-sm">
      <div className="text-gray-500 dark:text-gray-400 text-xs uppercase tracking-wide">
        Current Section
      </div>
      <div className="font-semibold text-gray-900 dark:text-white">
        {displayText}
      </div>
    </div>
  )
} 