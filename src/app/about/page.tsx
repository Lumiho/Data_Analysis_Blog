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
            Computer Science Student & Software Developer
          </p>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-4xl mx-auto px-4 py-12">
        {/* Personal Section */}
        <section className="mb-16">
          <div className="flex flex-col md:flex-row items-center md:items-center gap-8 md:gap-12">
            {/* Introduction Text */}
            <div className="flex-1 prose dark:prose-invert max-w-none">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Hello, I'm Leonardo Zavala
              </h2>
              <p className="text-lg text-gray-600 dark:text-gray-400 mb-4">
                I'm a senior at the University of California - Davis pursuing a <strong>Computer Science</strong> degree with a minor in <strong>Statistics</strong>. 
                My passion lies in developing efficient, functional <strong>software solutions</strong> and exploring <strong>data analysis</strong>. I combine 
                <strong> programming expertise</strong> with <strong>statistical knowledge</strong> to create meaningful applications and uncover valuable insights.
              </p>
              <p className="text-lg text-gray-600 dark:text-gray-400">
                This blog serves as both a learning journey and a platform to share my experiences in <strong>software development</strong> and <strong>data science</strong>. 
                Through hands-on projects and analysis, I focus on building <strong>robust solutions</strong> while exploring ways to derive significant 
                conclusions from data.
              </p>
            </div>
            
            {/* Profile Image */}
            <div className="flex-shrink-0 mb-6 md:mb-0">
              <img
                src="/about/Headshot_'24.jpg"
                alt="Leonardo Zavala Jimenez"
                className="w-56 h-56 md:w-64 md:h-64 object-cover rounded-2xl shadow-lg border-4"
                style={{ borderColor: '#B8860B' }}
              />
            </div>
          </div>
        </section>

        {/* Expertise Section */}
        <section className="mb-16">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Areas of Focus
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Technical Background */}
            <div className="bg-amber-50 dark:bg-amber-900/20 p-6 rounded-xl border border-amber-200 dark:border-amber-800">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                Technical Background
              </h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>Computer Science Major</li>
                <li>Statistics Minor</li>
                <li>Software Development</li>
                <li>Algorithm Design</li>
              </ul>
            </div>

            {/* Skills & Interests */}
            <div className="bg-amber-50 dark:bg-amber-900/20 p-6 rounded-xl border border-amber-200 dark:border-amber-800">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                Skills & Interests
              </h3>
              <ul className="space-y-2 text-gray-600 dark:text-gray-400">
                <li>Application Development</li>
                <li>Data Analysis & Visualization</li>
                <li>Machine Learning</li>
                <li>System Design</li>
              </ul>
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
            Let's Connect
          </h2>
          <div className="bg-gray-50 dark:bg-gray-800 p-6 rounded-xl border border-gray-200 dark:border-gray-700">
            <p className="text-gray-600 dark:text-gray-400 mb-4">
              I'm always eager to connect with fellow students, data enthusiasts, and industry professionals. 
              Whether you want to discuss potential collaborations, share insights, or just chat about data science, 
              feel free to reach out!
            </p>
            <div className="flex flex-wrap gap-4">
              <a
                href="https://www.linkedin.com/in/leonardo-zavala-jimenez-651801210"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-4 py-2 bg-[#B8860B] text-white rounded-full hover:bg-[#9A7009] transition-colors"
              >
                LinkedIn
              </a>
              <a
                href="mailto:zavalaleo715@yahoo.com"
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