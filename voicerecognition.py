import speech_recognition as sr
import cv2
import numpy as np
import re

def parse_arithmetic(text):
    # Replace spoken words with symbols for basic operations
    text = text.lower()
    text = text.replace("plus", "+").replace("add", "+")
    text = text.replace("minus", "-").replace("subtract", "-")
    text = text.replace("times", "*").replace("multiplied by", "*").replace("multiply", "*").replace("into", "*")
    text = text.replace("divide by", "/").replace("divided by", "/").replace("by", "/").replace("over", "/")
    text = text.replace("x", "*")

    # Remove non-arithmetic words
    match = re.match(r"([\d\.\s\+\-\*\/]+)", text)
    if match:
        expr = match.group(1)
        try:
            result = eval(expr)
            return f"{expr.strip()} = {result}"
        except Exception:
            return None
    return None

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    window_name = "Voice Recognition & Calculator - Say 'stop' to quit"

    display_img = np.zeros((200, 900, 3), dtype=np.uint8)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
            except sr.WaitTimeoutError:
                text = "(Listening...)"
            except sr.UnknownValueError:
                text = "(Could not understand)"
            except sr.RequestError:
                text = "(API unavailable)"
            except Exception as e:
                text = f"(Error: {e})"

            print(f"You said: {text}")

            # Check for stop command
            if "stop" in text.lower():
                print("Stop command detected. Exiting.")
                break

            # Check for arithmetic and calculate
            result = parse_arithmetic(text)
            if result:
                display_text = f"{text} => {result}"
            else:
                display_text = text

            # Display text on the image
            display_img[:] = 0
            cv2.putText(display_img, display_text, (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow(window_name, display_img)

            # Allow window close or 'q' to exit
            key = cv2.waitKey(100)
            if key == ord('q'):
                break
            if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()