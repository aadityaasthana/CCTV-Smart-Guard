# Demo Instructions

1. Create a virtual environment and install requirements: `pip install -r requirements.txt`.
2. Edit `config.json` if you want camera_source=0 (webcam) or RTSP URL.
3. Run `python app.py --config config.json` to start the processor.
4. In another terminal run `streamlit run dashboard_streamlit.py` to open the dashboard.
5. Simulate events (walk/run/lie down) in front of the camera and watch console for events and saved clips.