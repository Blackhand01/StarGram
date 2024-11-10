# Requirements Document - **Instagram Analysis and Optimization Tool**

## **Purpose**
The purpose of this project is to develop an application that helps Instagram users grow their online presence by optimizing posts and providing in-depth performance analysis. Through the integration of Gemini API and InstagAPI, the app will offer personalized suggestions to improve visibility and engagement by analyzing community and global market trends.

---

## **Stakeholders**
1. **Instagram Users**:
   - Content creators, influencers, and users aiming to optimize their Instagram presence.
2. **Marketers**:
   - Professionals using Instagram to promote brands, products, or services.
3. **Developers**:
   - Technical team leveraging Gemini and InstagAPI to implement functionalities.
4. **Community Managers**:
   - Individuals seeking to maximize audience engagement.

---

## **Functional Requirements**

### **1. Suggestions for New Posts**
Provide useful advice to create new posts that optimize visibility and engagement.
1. **Hashtag Suggestions**:
   - Identify effective hashtags based on local and global trends (using the *"GET Search Hashtag"* endpoint).

2. **Optimal Posting Times**:
   - Suggest the best times to post based on follower activity and historical post performance.

3. **Best Content Recommendations**:
   - Analyze local and global trends to recommend:
     - Popular content types (e.g., images, videos, stories).
     - Relevant themes based on the user's location or community (using the *"GET Location Posts"* endpoint).

4. **Caption Generation**:
   - Generate personalized captions based on:
     - Followers’ behaviors and interests (using the *"GET Similar Users"* endpoint).
     - Suitable sentiment and style via Gemini API.

---

### **2. Optimization of Existing Posts**
Provide suggestions for improving and enhancing engagement on already published posts.
1. **Performance Analysis**:
   - Analyze key metrics for existing posts (using the *"GET Post Detail"* endpoint):
     - Number of likes, comments, views, reposts, and shares.
   - Classify content based on best and worst performance.

2. **Comparison with Similar Posts**:
   - Compare the existing post with:
     - Similar posts with higher engagement.
     - Posts published in the same location (using the *"GET Location Posts"* endpoint).

3. **Improvement Suggestions**:
   - Propose changes based on:
     - Better use of hashtags and captions.
     - Optimization of images/videos through predictive analysis from Gemini API.

---

### **3. Additional Features**

1. **Music Analysis in Posts**:
   - **Endpoint**: *"GET Music Posts"*.  
   - **Functionality**:
     - Analyze music used in the most popular posts.
     - Suggest trending tracks for new content.

---

### **4. Future Features (not ready for the hackathon)**

1. **Follower Analysis**:
   - **Endpoint**: *"GET User Followers"* / *"GET User Following"*.  
   - **Functionality**:
     - Identify the most active followers.
     - Suggest new users to follow to increase interactions.

2. **Live Broadcast Analysis**:
   - **Endpoint**: *"GET Live Broadcast Info"* / *"GET Live Broadcast Comments"*.  
   - **Functionality**:
     - Integrate analysis features for live broadcasts.
     - Suggest optimal times and topics of interest.

3. **Product Analysis for Business Accounts**:
   - **Endpoint**: *"GET Product Info"*.  
   - **Functionality**:
     - Analyze product performance in the Instagram shop.
     - Suggest improvements for descriptions or images.

4. **Tagged Post Analysis**:
   - **Endpoint**: *"GET User Tagged Posts"*.  
   - **Functionality**:
     - Identify posts where the user is tagged.
     - Analyze their performance to discover potential collaborations or successful content.

---

## **Non-Functional Requirements**
1. **Usability**:
   - The backend interface must be clear and well-documented for future integrations.

2. **Performance**:
   - The app must process a request in under 2 seconds (API limit).

3. **Scalability**:
   - Support multiple requests without exceeding InstagAPI limits.

4. **Reliability**:
   - Handle API errors (e.g., request limits) with clear messages and fallback options.

---

## **Limitations**
1. The app can only analyze public profiles or those for which the user has explicitly granted consent.
2. **InstagAPI Limits**:
   - Maximum of 50 requests in the free version.
   - Limited access to hashtag data for unlinked users.
3. **Gemini API Limits**:
   - Dependency on predictive and multimodal analysis subject to daily usage limits.
4. Geographic and music data may be incomplete in certain regions.

---

## **Technologies Used**
- **Backend**: Python with FastAPI for development speed and performance.
- **APIs**:
  - **InstagAPI**: For gathering profile, post, hashtag, and location data.
  - **Gemini AI API**: For advanced analysis and suggestion generation.
- **Database**: SQLite for simplicity in data management during the hackathon.

---

## **Hackathon Roadmap**

### **Phase 1: API Integration (November 8, evening)**
**Objective**: Connect the application to Instagram and Gemini APIs to collect data and generate suggestions.  
- **Activities**:
  1. Configure authentication with InstagAPI.
  2. Connect with Gemini API for predictive analysis.
  3. Create basic endpoints in `src/main.py` for:
     - Post statistics (e.g., endpoint "Get Instagram Post Details").
     - Personalized suggestions (e.g., endpoint "Get Instagram Search Hashtags").

**Expected Output**:
- Functional endpoints for data collection and suggestions.
- Tested code with mock APIs and `tests/test_main.py`.

---

### **Phase 2: Analysis Logic and Suggestions (November 9, morning)**
**Objective**: Implement the logic to analyze data and generate useful suggestions.  
- **Activities**:
  1. Create analysis functions in `src/main.py`:
     - Interaction analysis for posts and stories.
     - Identification of optimal posting times.
     - Generation of personalized captions.
  2. Test functions with real cases using live APIs and test scripts.

**Expected Output**:
- Complete functionalities for analysis and suggestions.
- Results displayed in JSON format (ready for testing and future integrations).

---

### **Phase 3: Testing and Documentation (November 9, afternoon)**
**Objective**: Ensure all features are tested and well-documented.  
- **Activities**:
  1. Run unit and integration tests with `pytest`.
  2. Document API endpoints in:
     - `README.md`: Instructions for using the project.
     - `SETUP.md`: Guide for configuring the APIs.
  3. Clean the code and update `requirements.txt`.

**Expected Output**:
- Complete tests and clear documentation.
- Code ready for review and delivery.

---

### **Phase 4: Final Debugging and Demo Preparation (November 10, morning)**
**Objective**: Fix bugs and prepare a functional demo.  
- **Activities**:
  1. Run end-to-end tests with real cases.
  2. Create a demo script to showcase:
     - Data collection statistics.
     - Generation of personalized suggestions.
  3. Clean up the repository and prepare for submission.

**Expected Output**:
- Fully functional project ready for evaluation.
- Organized and documented repository.

---
