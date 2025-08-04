"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Search, Sun } from "lucide-react";

const startupData = [
  {
    name: "TechSolutions Inc.",
    domain: "AI in Logistics",
    verdict: "Strong Buy",
    score: 95,
    scoreWidth: "100%",
  },
  {
    name: "InnovateLogistics",
    domain: "AI in Logistics", 
    verdict: "Hold",
    score: 75,
    scoreWidth: "75%",
  },
  {
    name: "SwiftAI",
    domain: "AI in Logistics",
    verdict: "Avoid", 
    score: 40,
    scoreWidth: "40%",
  },
  {
    name: "LogiTech AI",
    domain: "AI in Logistics",
    verdict: "Strong Buy",
    score: 90,
    scoreWidth: "90%",
  },
  {
    name: "FutureLogistics",
    domain: "AI in Logistics",
    verdict: "Hold",
    score: 65,
    scoreWidth: "65%",
  },
];

export default function Home() {
  const [searchQuery, setSearchQuery] = useState("");
  const [activeTab, setActiveTab] = useState("startup");

  return (
    <div className="min-h-screen bg-venture-dark text-white">
      {/* Header */}
      <header className="border-b border-[#E5E8EB] px-6 sm:px-10 py-3">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <div className="flex items-center gap-4">
            <div className="w-4 h-4 relative">
              <svg className="w-4 h-4 fill-white" viewBox="0 0 14 14">
                <path fillRule="evenodd" clipRule="evenodd" d="M13.6667 0.333333H9.2222V4.7778H4.7778V9.2222H0.333333V13.6667H13.6667V0.333333Z" />
              </svg>
            </div>
            <span className="text-lg font-bold text-white">VentureViz</span>
          </div>

          {/* Navigation */}
          <div className="hidden md:flex items-center gap-8">
            <nav className="flex items-center gap-9">
              <span className="text-sm text-white cursor-pointer">Home</span>
              <span className="text-sm text-white cursor-pointer">About</span>
              <span className="text-sm text-white cursor-pointer">Contact</span>
            </nav>
            
            <div className="flex items-center gap-2">
              <Button className="bg-venture-blue text-venture-dark font-bold text-sm px-4 py-2 h-10 rounded-xl hover:bg-venture-blue/90">
                Get Started
              </Button>
              <Button variant="ghost" size="sm" className="bg-venture-gray text-white h-10 w-10 p-0 rounded-xl hover:bg-venture-gray/80">
                <Sun className="w-5 h-5" />
              </Button>
            </div>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <Button className="bg-venture-blue text-venture-dark font-bold text-sm px-4 py-2 h-10 rounded-xl">
              Get Started
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="px-6 sm:px-10 lg:px-40 py-5">
        <div className="max-w-6xl mx-auto">
          {/* Hero Section */}
          <div className="p-4">
            <div 
              className="relative min-h-[480px] rounded-xl overflow-hidden bg-cover bg-center"
              style={{
                backgroundImage: `linear-gradient(90deg, rgba(0, 0, 0, 0.10) 0%, rgba(0, 0, 0, 0.40) 100%), url('https://cdn.builder.io/api/v1/assets/375c9251959c4f5f832234416757eb27/figma-screenshot-a1dafe?format=webp&width=800')`
              }}
            >
              {/* Hero Content Positioned - Desktop */}
              <div className="hidden lg:block absolute left-1/2 top-[235px] transform -translate-x-1/2 w-full max-w-4xl text-center px-8">
                <h1 className="text-5xl font-black text-white leading-[60px] mb-2 tracking-[-2px]">
                  AI-Powered VC Scouting
                </h1>
                <p className="text-base text-white leading-6 max-w-2xl mx-auto">
                  Automate your venture capital scouting process with our agent-based system. Identify promising startups, analyze market trends, and generate investment summaries.
                </p>
              </div>

              {/* Hero Content - Mobile/Tablet */}
              <div className="lg:hidden flex flex-col justify-end items-center h-full p-8 pb-16">
                <div className="text-center max-w-md mb-8">
                  <h1 className="text-3xl sm:text-4xl font-black text-white leading-tight mb-4 tracking-tight">
                    AI-Powered VC Scouting
                  </h1>
                  <p className="text-sm sm:text-base text-white leading-6">
                    Automate your venture capital scouting process with our agent-based system. Identify promising startups, analyze market trends, and generate investment summaries.
                  </p>
                </div>
                
                {/* Mobile Search Bar */}
                <div className="w-full max-w-sm">
                  <div className="flex rounded-xl border border-venture-light bg-venture-darker overflow-hidden">
                    <div className="flex items-center pl-3">
                      <Search className="w-4 h-4 text-venture-text" />
                    </div>
                    <Input
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      placeholder="Enter domain"
                      className="flex-1 bg-transparent border-0 text-venture-text placeholder:text-venture-text focus-visible:ring-0 px-2 py-2 h-10 text-sm"
                    />
                    <Button className="bg-venture-blue text-venture-dark font-bold px-4 py-2 m-1 rounded-xl hover:bg-venture-blue/90 h-10 text-sm">
                      Search
                    </Button>
                  </div>
                </div>
              </div>

              {/* Search Bar Positioned - Desktop Only */}
              <div className="hidden lg:block absolute left-1/2 top-[383px] transform -translate-x-1/2 w-full max-w-lg px-8">
                <div className="flex rounded-xl border border-venture-light bg-venture-darker overflow-hidden">
                  <div className="flex items-center pl-4">
                    <Search className="w-5 h-5 text-venture-text" />
                  </div>
                  <Input
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    placeholder="Enter  domain (e.g. AI in logistics)"
                    className="flex-1 bg-transparent border-0 text-venture-text placeholder:text-venture-text focus-visible:ring-0 px-2 py-2 h-12"
                  />
                  <Button className="bg-venture-blue text-venture-dark font-bold px-5 py-3 m-2 rounded-xl hover:bg-venture-blue/90 h-12">
                    Search
                  </Button>
                </div>
              </div>
            </div>
          </div>

          {/* Progress Section */}
          <div className="p-4">
            <div className="mb-3">
              <h3 className="text-base font-medium text-white mb-3">Agent Task Completion</h3>
              <div className="w-full bg-venture-light rounded h-2 overflow-hidden">
                <div className="h-full bg-white rounded" style={{ width: "60%" }}></div>
              </div>
              <p className="text-sm text-venture-text mt-3">60%</p>
            </div>
          </div>

          {/* Tabs */}
          <div className="pb-3">
            <div className="px-4 border-b border-venture-light">
              <div className="flex gap-8">
                <button
                  onClick={() => setActiveTab("startup")}
                  className={`py-4 text-sm font-bold border-b-[3px] ${
                    activeTab === "startup"
                      ? "text-white border-[#E5E8EB]"
                      : "text-venture-text border-[#E5E8EB]"
                  }`}
                >
                  Startup list
                </button>
                <button
                  onClick={() => setActiveTab("trend")}
                  className={`py-4 text-sm font-bold border-b-[3px] ${
                    activeTab === "trend"
                      ? "text-white border-[#E5E8EB]"
                      : "text-venture-text border-[#E5E8EB]"
                  }`}
                >
                  Trend analysis
                </button>
                <button
                  onClick={() => setActiveTab("investment")}
                  className={`py-4 text-sm font-bold border-b-[3px] ${
                    activeTab === "investment"
                      ? "text-white border-[#E5E8EB]"
                      : "text-venture-text border-[#E5E8EB]"
                  }`}
                >
                  Investment summary
                </button>
              </div>
            </div>
          </div>

          {/* Data Table */}
          <div className="p-3">
            <div className="rounded-xl border border-venture-light bg-venture-dark overflow-x-auto">
              <div className="min-w-[800px]">
                {/* Table Header */}
                <div className="bg-venture-darker flex">
                  <div className="flex-1 px-4 py-3 text-sm font-medium text-white min-w-[200px]">Startup</div>
                  <div className="w-56 px-4 py-3 text-sm font-medium text-white">Domain</div>
                  <div className="w-48 px-4 py-3 text-sm font-medium text-white">Verdict</div>
                  <div className="w-64 px-4 py-3 text-sm font-medium text-white">Score</div>
                </div>

                {/* Table Rows */}
                {startupData.map((startup, index) => (
                  <div key={index} className="flex border-t border-[#E5E8EB]">
                    <div className="flex-1 px-4 py-6 text-sm text-white flex items-center min-w-[200px]">
                      {startup.name}
                    </div>
                    <div className="w-56 px-4 py-6 text-sm text-venture-text flex items-center">
                      {startup.domain}
                    </div>
                    <div className="w-48 px-4 py-6 flex items-center">
                      <span className="bg-venture-gray text-white px-4 py-2 rounded-xl text-sm font-medium whitespace-nowrap">
                        {startup.verdict}
                      </span>
                    </div>
                    <div className="w-64 px-4 py-6 flex items-center">
                      <div className="flex items-center gap-3 w-full">
                        <div className="flex-1 bg-venture-light rounded-sm h-1 overflow-hidden min-w-[60px]">
                          <div 
                            className="h-full bg-white rounded-sm" 
                            style={{ width: startup.scoreWidth }}
                          ></div>
                        </div>
                        <span className="text-sm text-white font-medium w-6">
                          {startup.score}
                        </span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t-0 px-6 sm:px-10 lg:px-40">
        <div className="max-w-6xl mx-auto py-10">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-6 mb-6">
            <div className="flex gap-8">
              <span className="text-base text-venture-text cursor-pointer">Privacy Policy</span>
              <span className="text-base text-venture-text cursor-pointer">Terms of Service</span>
            </div>
            
            <div className="flex items-center gap-4">
              <button className="text-venture-text hover:text-white transition-colors">
                <svg className="w-6 h-6" viewBox="0 0 21 19" fill="currentColor">
                  <path fillRule="evenodd" clipRule="evenodd" d="M20.1928 3.46313C20.0768 3.18285 19.8033 3.00006 19.5 3H16.6472C15.8359 1.61972 14.3604 0.765791 12.7594 0.75C11.5747 0.734462 10.4339 1.19754 9.59531 2.03438C8.73219 2.88138 8.24717 4.04071 8.25 5.25V5.82094C4.47563 4.82531 1.38844 1.755 1.35563 1.72219C1.15019 1.51493 0.843182 1.44566 0.568648 1.54461C0.294115 1.64356 0.101905 1.89277 0.0759375 2.18344C-0.328125 6.66375 0.973125 9.66187 2.13844 11.3878C2.70664 12.241 3.39786 13.0055 4.18969 13.6566C2.76188 15.3 0.51375 16.1634 0.489375 16.1728C0.274975 16.2531 0.108995 16.4269 0.0386822 16.6448C-0.031631 16.8627 0.00142384 17.1008 0.128438 17.2913C0.19875 17.3962 0.48 17.7647 1.16719 18.1087C2.01656 18.5344 3.13875 18.75 4.5 18.75C11.1253 18.75 16.6612 13.6481 17.2266 7.08375L20.0306 4.28062C20.2451 4.06601 20.3091 3.74335 20.1928 3.46313ZM15.9741 6.22031C15.8455 6.34921 15.7682 6.52049 15.7566 6.70219C15.375 12.6169 10.4325 17.25 4.5 17.25C3.51 17.25 2.8125 17.1187 2.32312 16.9613C3.40219 16.3753 4.90688 15.3675 5.87438 13.9163C5.98915 13.7438 6.02746 13.5315 5.98023 13.3298C5.93299 13.128 5.80442 12.9548 5.625 12.8512C5.58094 12.8259 1.50844 10.3819 1.5 3.85125C3 5.07 5.74219 6.96094 8.87531 7.48781C9.09265 7.52446 9.3151 7.46364 9.48358 7.32154C9.65205 7.17943 9.74949 6.9704 9.75 6.75V5.25C9.7483 4.44176 10.0728 3.66702 10.65 3.10125C11.2034 2.54686 11.9574 2.23983 12.7406 2.25C13.9275 2.265 15.0366 2.98875 15.5006 4.05094C15.6202 4.32382 15.8899 4.50008 16.1878 4.5H17.6878L15.9741 6.22031Z" />
                </svg>
              </button>
              <button className="text-venture-text hover:text-white transition-colors">
                <svg className="w-6 h-6" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" clipRule="evenodd" d="M18.25 0.25H1.75C0.921573 0.25 0.25 0.921573 0.25 1.75V18.25C0.25 19.0784 0.921573 19.75 1.75 19.75H18.25C19.0784 19.75 19.75 19.0784 19.75 18.25V1.75C19.75 0.921573 19.0784 0.25 18.25 0.25ZM18.25 18.25H1.75V1.75H18.25V18.25ZM7 8.5V14.5C7 14.9142 6.66421 15.25 6.25 15.25C5.83579 15.25 5.5 14.9142 5.5 14.5V8.5C5.5 8.08579 5.83579 7.75 6.25 7.75C6.66421 7.75 7 8.08579 7 8.5ZM15.25 11.125V14.5C15.25 14.9142 14.9142 15.25 14.5 15.25C14.0858 15.25 13.75 14.9142 13.75 14.5V11.125C13.75 10.0895 12.9105 9.25 11.875 9.25C10.8395 9.25 10 10.0895 10 11.125V14.5C10 14.9142 9.66421 15.25 9.25 15.25C8.83579 15.25 8.5 14.9142 8.5 14.5V8.5C8.50193 8.11975 8.78811 7.80112 9.16598 7.75852C9.54384 7.71592 9.89378 7.96285 9.98031 8.33313C11.0142 7.63174 12.351 7.55891 13.455 8.14381C14.559 8.7287 15.2496 9.87563 15.25 11.125ZM7.375 5.875C7.375 6.49632 6.87132 7 6.25 7C5.62868 7 5.125 6.49632 5.125 5.875C5.125 5.25368 5.62868 4.75 6.25 4.75C6.87132 4.75 7.375 5.25368 7.375 5.875Z" />
                </svg>
              </button>
            </div>
          </div>
          
          <div className="text-center">
            <p className="text-base text-venture-text">© 2024 VentureViz. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
