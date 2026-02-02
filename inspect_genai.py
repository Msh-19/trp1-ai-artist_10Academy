try:
    from google import genai
    from google.genai import types
    print("google.genai.types attributes:")
    for attr in dir(types):
        if "Video" in attr:
            print(f" - {attr}")
except ImportError:
    print("google-genai not installed")
except Exception as e:
    print(f"Error: {e}")
