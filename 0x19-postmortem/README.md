# 0x19. Postmortem

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

- To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

![Postmortem Report](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bSUlrrO7E83Eb85sAIiZrw.png)



# 🚨 **Postmortem Report: The Day the Memory Leak Struck** 🚨

![Escalation](https://miro.medium.com/v2/resize:fit:1172/format:webp/1*ty95YKSBnrpgSZ-_abaOIA.png)
*When the server suffers from memory leak....*

## Issue Summary

- **Duration:** The Great Memory Meltdown lasted for **2 hours and 45 minutes** from **3:15 PM to 6:00 PM UTC** on **August 12, 2024**.
  
- **Impact:** During the outage, our e-commerce website transformed from a sleek shopping experience to a sluggish beast. Users were clicking furiously, only to be met with spinning wheels and failed transactions. Approximately **85% of users** faced the wrath of the slow-down monster, and **20%** couldn’t complete their purchases. Our sales team mourned the temporary revenue loss, and our customer service team suddenly became best friends with the word "Sorry!"

- **Root Cause:** Turns out, our servers weren’t trying to take a nap; they were just choking on a memory leak in the session management service. The leak caused our servers to hog memory like it was going out of style, leading to the unfortunate slow-down.

## Timeline

Here’s how our day of doom unfolded:

- **3:15 PM UTC:** 🎯 Issue detected via a monitoring alert screaming “High memory usage!”
- **3:17 PM UTC:** 😱 Incident escalated to the on-call DevOps engineer, who was dreaming of a peaceful afternoon.
- **3:20 PM UTC:** 🕵️‍♂️ The blame game began. Was it the database again? (Spoiler: It wasn’t.)
- **3:35 PM UTC:** 💡 Database cleared of all charges; investigation shifted to the load balancer.
- **4:00 PM UTC:** 🔍 Ah-ha! Server metrics pointed to a memory leak. Our servers weren’t bloated; they were just full of unwanted junk!
- **4:20 PM UTC:** 🔎 The session management service, recently updated with fancy new features, was singled out as the main suspect.
- **4:45 PM UTC:** 🚨 Incident escalated to the developers who built the session management service.
- **5:15 PM UTC:** 🛠️ Developers confirmed the presence of the leak. Time to plug it!
- **5:45 PM UTC:** 🔧 A patch was deployed to kick the memory leak out.
- **6:00 PM UTC:** 🟢 All systems go! The website was back to its former glory.

## Root Cause and Resolution

- **Root Cause:** Our session management service was hoarding memory like a squirrel hoards nuts for winter. Session objects weren’t being properly released from memory, causing the servers to eventually buckle under the weight. The culprit? A recent update that introduced a new session tracking feature but forgot to pack the garbage bags.

- **Resolution:** Our sharp-eyed developers jumped in, pinpointed the faulty code, and implemented a patch. This fix made sure session objects were correctly garbage-collected, so our servers could breathe easy again. After some rigorous testing in the staging environment, the patch was rolled out to production, and peace was restored.

## Corrective and Preventative Measures

Let’s make sure this doesn’t happen again:

- **Improvements:**
  1. **Code Review Process:** We’re beefing up our code reviews to catch memory management mishaps before they hit production.
  2. **Monitoring Enhancements:** We’re adding extra eyes on memory usage in the session management service to catch leaks before they become a deluge.
  3. **Load Testing:** Our load tests will now include long-duration stress tests, so we can spot memory issues lurking in the shadows.

- **Tasks:**
  1. **Patch Nginx server** to improve session handling and reduce memory overhead.
  2. **Add memory usage monitoring** to our APM tool, focused on the session management service.
  3. **Review and refactor the session management service codebase** to ensure it plays nicely with memory.
  4. **Conduct a post-incident review** with the dev team to brainstorm further improvements.
  5. **Document best practices** for memory management in our development guidelines.

![Memory Leak Diagram](https://resources.jetbrains.com/help/img/idea/2024.2/cpu-memory-charts-leak_dark.png)  
*Figure 1: How the memory leak took down our servers.*

