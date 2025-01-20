# Real-Time Transcription & Video Processing Service

## Overview

This project implements a **Real-Time Transcription System** for meetings and audio content, leveraging **OpenAI's Whisper API** for speech-to-text conversion and **GPT-3.5 API** for summarization. Additionally, **FFmpeg** is used for video-to-audio conversion. The service supports both **video uploads** and **live audio streams**, providing features like **transcription**, **summarization**, and **translation**.

## Core Features

1. **Video Upload & Audio Extraction**:
   - Users can upload video files.
   - Audio is extracted from video files using **FFmpeg**.

2. **Speech-to-Text Conversion (Whisper API)**:
   - The extracted audio (from uploaded videos or live audio) is sent to **OpenAI's Whisper API** for transcription.

3. **Summarization**:
   - After transcribing the audio to text, the transcript is sent to **GPT-3.5 API** to generate summaries, key points, and action items.

4. **Translation (Optional)**:
   - The transcript or summary can be translated into different languages using **OpenAI’s Translation Models** or other translation services.

5. **Real-Time Transcription**:
   - For live audio, real-time transcription is supported via **WebSocket** (or other streaming protocols) using **Whisper API** and **Python threading/queue** system for concurrent processing.