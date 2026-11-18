# AI Lab Test 2: Demonstration Video Submission

**Course:** Artificial Intelligence Lab (IC-709D / IC-703 C)  
**Student Name:** Khushi Dixit  
**Roll Number:** 51 (University Roll: IC-2K23-51)  
**Subject:** Artificial Intelligence  
**Assignment:** Lab Test 2  
**Assigned Set:** Set 1 – Smart Traffic Signal Controller  

---

## 📹 Practical Demonstration Video Link

* **Student:** Khushi Dixit  
* **Roll Number:** 51 (IC-2K23-51)  
* **Video Demonstration Link:** `[PASTE YOUR DEMO VIDEO LINK HERE]`  

---

## 📋 Instructions for Recording & Submitting Your Video

As per the faculty's examination instructions, this practical exam requires a video demonstration walking through the code and executing the program. Please follow these steps:

### Step 1: Record Your Demonstration
- Use screen recording software (e.g., OBS Studio, Windows Game Bar `Win + G`, Zoom, or Loom).
- Introduce yourself clearly: State your name (**Khushi Dixit**), roll number (**51 / IC-2K23-51**), and topic (**Set 1: Smart Traffic Signal Controller in Turbo Prolog**).
- Walk through the code in `smart_traffic_controller.pro`:
  - Explain the `DOMAINS` and dynamic `DATABASE` facts.
  - Explain Rule 1 (Emergency Priority: $10,000 + 10 \times \text{Wait} + \text{Vehicles}$).
  - Explain Rule 2 (Blocked Road safety exclusion: Score = $-1$).
  - Explain Rules 3, 4, 5 (Normal traffic: Density Weight $+ 2 \times \text{Vehicles} + 3 \times \text{Wait}$).
  - Explain Rule 6 (Tie-breaking: Wait Time $\rightarrow$ Vehicle Count $\rightarrow$ Road Rank).

### Step 2: Demonstrate the Test Scenarios
Demonstrate the execution of the program across the core test scenarios:
1. **Benchmark Scenario:** Road B has an emergency vehicle and gets GREEN over Road C with 25 vehicles.
2. **Normal Peak Scenario:** No emergency; Road C gets GREEN due to high volume.
3. **Blocked Road Scenario:** Road C is blocked due to an accident; Road B gets GREEN instead.
4. **Tie Scenario:** Road A and Road D tied at score 68; Road A wins via canonical road rank.
5. **Interactive Mode:** Enter custom values live to demonstrate dynamic handling.

### Step 3: Upload the Video
- **Option A (Google Drive):**
  - Upload your MP4 recording to Google Drive.
  - Right-click the file $\rightarrow$ **Share** $\rightarrow$ Under "General access", select **Anyone with the link – Viewer**.
  - Copy the shareable link.
- **Option B (YouTube):**
  - Upload the video to YouTube.
  - Set the visibility to **Unlisted** (so only individuals with the link can view it).
  - Copy the YouTube video URL.

### Step 4: Update This Submission
- Open `README.md` and this `DEMO_VIDEO.md`.
- Replace `[PASTE YOUR DEMO VIDEO LINK HERE]` with your actual link.
- Save and push the commit to your GitHub repository:
  ```bash
  git add README.md DEMO_VIDEO.md
  git commit -m "Update practical demonstration video link"
  git push origin main
  ```
