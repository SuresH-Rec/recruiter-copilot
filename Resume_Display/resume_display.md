 def __init__(self):
        self.name = "Suresh Korumilli"
        self.title = "Senior Talent Acquisition Professional | 7+ Years in Tech Hiring"
        self.contact = {
            "Phone": "0000000000",
            "Email": "sureshvenkataramana7@gmail.com",
            "LinkedIn": "linkedin.com/in/sureshvenkataramana",
            "GitHub": "github.com/SuresH-Rec",
            "Location": "Bengaluru",
        }
        self.summary = (
            "Results-driven Senior TA Professional with 7+ years of full-cycle "
            "tech recruitment experience across GCC, product companies, MNCs, "
            "and startups. Deep expertise in niche hiring for AI/ML, RPA, GenAI, "
            "Cloud, Data, and Full-Stack roles. Skilled in stakeholder management, "
            "Boolean sourcing, vendor coordination, and data-driven recruiting "
            "using Power BI dashboards. Track record of 90%+ offer acceptance, "
            "25-30% reduction in time-to-fill, and building scalable talent "
            "pipelines. Currently upskilling in AI-assisted recruitment and "
            "automation, building practical tools to enhance sourcing, "
            "screening, and reporting workflows."
        )
        self.experience = [
            {
                "role": "Talent Acquisition Specialist",
                "duration": "Sep 2025 – Present",
                "company": "Acronotics Pvt Ltd — AI-Focused Services & Product Startup | Bengaluru",
                "highlights": [
                    "Owned end-to-end TA for an AI-focused startup across RPA, Automation, AI/ML, Data, Cloud, and low-code domains.",
                    "Achieved 80% fulfillment of hiring requirements by aligning strategy with leadership and enterprise clients.",
                    "Built and maintained 500+ candidate talent pools, reducing time-to-hire by 30%.",
                    "Boosted candidate engagement by 40% and offer acceptance to 90% via employer branding.",
                    "Supported hiring across 10 enterprise clients.",
                ],
            },
            {
                "role": "Senior Recruiter",
                "duration": "Nov 2023 – May 2024",
                "company": "ITC Infotech | Bengaluru",
                "highlights": [
                    "Delivered 100% on-time closures within SLA-aligned timelines for UK and global tech clients.",
                    "Managed 7+ vendors and 3 sourcing channels; cut time-to-fill by 25% for niche tech roles.",
                    "Increased offer acceptance by 20% and boosted direct hires by 60%.",
                ],
            },
            {
                "role": "HR Executive",
                "duration": "May 2022 – Sep 2023",
                "company": "DanskeIT (Alchemy Techsol Pvt Ltd) | Bengaluru",
                "highlights": [
                    "Closed 40+ positions with a 95% offer-to-join ratio.",
                    "Partnered with 15+ hiring managers; scaled capacity by 50% through vendor partnerships.",
                    "Increased qualified submissions by 35% and reduced candidate drop-offs by 20%.",
                ],
            },
            {
                "role": "Senior Recruitment Executive",
                "duration": "Sep 2019 – Apr 2022",
                "company": "Han Digital Solutions | Bengaluru",
                "highlights": [
                    "Managed 50+ recruitment mandates simultaneously across multiple clients.",
                    "Mentored 3 junior recruiters and collaborated with 10+ clients on hiring strategy.",
                ],
            },
            {
                "role": "Associate Recruitment Executive",
                "duration": "Feb 2018 – Aug 2019",
                "company": "Aimplus Staffing Solution | Bengaluru",
                "highlights": [
                    "Sourced and screened 100+ junior to mid-level candidates across tech domains.",
                    "Improved recruiter response rate by 40% through structured follow-ups.",
                ],
            },
        ]
        self.core_skills = {
            "Sourcing & Search": "Full-cycle recruitment, Boolean search, LinkedIn Recruiter, Naukri, AI-assisted sourcing, passive candidate engagement, niche & leadership hiring",
            "Tech Domains": "AI/ML, RPA, GenAI, Cloud (AWS/Azure/GCP), Full-Stack, Data Science, DevOps, Cybersecurity, Low-code, SAP, Oracle",
            "Tools & Platforms": "ATS (Taleo, Workday, SuccessFactors, Oracle Cloud, PeopleSoft), Power BI, Excel, Microsoft 365, Google Suite, CRM platforms",
            "Stakeholder Mgmt": "Hiring manager collaboration, SLA management, client relationship management, vendor coordination, escalation handling",
            "Emerging & Tech": "Recruiter Copilot (AI workflow), Python scripting, Power Automate, prompt engineering, recruitment automation, dashboard design",
        }
        self.certifications = [
            "Analyzing & Visualizing Data with Power BI — Edu4Sure",
            "Google Project Management — Coursera",
            "HR Analyst Professional — VSKILLS",
            "Diploma in Human Resource Management — Alison",
            "GEM Award — Excellence in Recruiting Outcomes, DanskeIT, 2022–2023",
        ]
        self.education = {
            "degree": "Bachelor of Technology (B.Tech)",
            "duration": "2010 – 2014",
            "institution": "A.K.R.G College of Engineering and Technology, West Godavari, AP",
        }

    def display_header(self):
        print("=" * 70)
        print(f"{self.name.upper()}")
        print(f"{self.title}")
        print("=" * 70)
        for key, value in self.contact.items():
            print(f"{key:10}: {value}")
        print("-" * 70)

    def display_summary(self):
        print("\nPROFESSIONAL SUMMARY")
        print("-" * 70)
        print(self.summary)

    def display_experience(self):
        print("\nPROFESSIONAL EXPERIENCE")
        print("-" * 70)
        for job in self.experience:
            print(f"\n{job['role']} | {job['duration']}")
            print(f"{job['company']}")
            for point in job["highlights"]:
                print(f" • {point}")

    def display_core_skills(self):
        print("\nCORE SKILLS")
        print("-" * 70)
        for category, skills in self.core_skills.items():
            print(f"{category:20}: {skills}")

    def display_certifications(self):
        print("\nCERTIFICATIONS & AWARDS")
        print("-" * 70)
        for cert in self.certifications:
            print(f" • {cert}")

    def display_education(self):
        print("\nEDUCATION")
        print("-" * 70)
        print(f"{self.education['degree']} ({self.education['duration']})")
        print(f"{self.education['institution']}")

    def display_full_profile(self):
        self.display_header()
        self.display_summary()
        self.display_experience()
        self.display_core_skills()
        self.display_certifications()
        self.display_education()
        print("\n" + "=" * 70)


def main():
    """Console menu to navigate profile sections."""
    profile = Profile()

    menu = {
        "1": ("View Full Profile", profile.display_full_profile),
        "2": ("View Summary", profile.display_summary),
        "3": ("View Experience", profile.display_experience),
        "4": ("View Core Skills", profile.display_core_skills),
        "5": ("View Certifications", profile.display_certifications),
        "6": ("View Education", profile.display_education),
        "0": ("Exit", None),
    }

    while True:
        print("\nPROFILE MENU")
        for key, (label, _) in menu.items():
            print(f" {key}. {label}")

        choice = input("\nSelect an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
