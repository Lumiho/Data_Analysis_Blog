export default function AboutPage() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-900">
      {/* Header */}
      <div className="relative bg-gradient-to-r from-blue-600 to-indigo-700 py-16 px-4">
        <div className="pattern-overlay absolute inset-0 opacity-40"></div>
        <div className="max-w-4xl mx-auto text-center relative z-10">
          <h1 className="text-4xl font-bold text-white mb-4">
            About Me
          </h1>
          <p className="text-xl text-blue-100">
            Data Analyst & Technical Writer
          </p>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-4xl mx-auto px-4 py-12">
        {/* Personal Section */}
        <section className="mb-16">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Hello, I'm [Your Name]
          </h2>
          <div className="prose dark:prose-invert">
            <p className="text-lg text-gray-600 dark:text-gray-400">
              I'm a passionate data analyst with expertise in transforming complex data into actionable insights. 
              With over [X] years of experience in data analysis and visualization, I've helped organizations 
              make data-driven decisions and uncover valuable patterns in their data.
            </p>
            <p className="text-lg text-gray-600 dark:text-gray-400 mt-4">
              Through this blog, I share my knowledge and experiences in data analysis, 
              machine learning, and modern development practices. My goal is to make data science 
              more accessible and help others learn from real-world examples and practical tutorials.
            </p>
          </div>
        </section>

        {/* Expertise Section */}
        <section className="mb-16">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Areas of Expertise
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Data Analysis */}
            <div className="bg-gray-50 dark:bg-gray-800 p-6 rounded-xl border border-gray-200 dark:border-gray-700">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                Data Analysis
              </h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>Statistical Analysis</li>
                <li>Data Visualization</li>
                <li>Predictive Modeling</li>
                <li>Business Intelligence</li>
              </ul>
            </div>

            {/* Technical Skills */}
            <div className="bg-gray-50 dark:bg-gray-800 p-6 rounded-xl border border-gray-200 dark:border-gray-700">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                Technical Skills
              </h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>Python (Pandas, NumPy, Scikit-learn)</li>
                <li>R Programming</li>
                <li>SQL & Database Management</li>
                <li>Data Visualization Tools (Tableau, Power BI)</li>
              </ul>
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Get in Touch
          </h2>
          <div className="bg-gray-50 dark:bg-gray-800 p-6 rounded-xl border border-gray-200 dark:border-gray-700">
            <p className="text-gray-600 dark:text-gray-400 mb-4">
              I'm always interested in connecting with fellow data enthusiasts and potential collaborators. 
              Feel free to reach out through any of the following channels:
            </p>
            <div className="flex flex-wrap gap-4">
              <a
                href="https://twitter.com/yourusername"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-4 py-2 bg-[#B8860B] text-white rounded-full hover:bg-[#9A7009] transition-colors"
              >
                Twitter
              </a>
              <a
                href="https://linkedin.com/in/yourusername"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-4 py-2 bg-[#B8860B] text-white rounded-full hover:bg-[#9A7009] transition-colors"
              >
                LinkedIn
              </a>
              <a
                href="mailto:your.email@example.com"
                className="inline-flex items-center px-4 py-2 bg-[#B8860B] text-white rounded-full hover:bg-[#9A7009] transition-colors"
              >
                Email
              </a>
            </div>
          </div>
        </section>
      </div>
    </div>
  )
} 