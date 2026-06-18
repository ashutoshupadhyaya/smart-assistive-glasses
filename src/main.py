from object_detection import object_detection
from ocr import read_text
from ultrasonic import detect_obstacles

def main():
    print("Smart Glasses System Ready")

    while True:
        print("\n1. Object Detection")
        print("2. OCR")
        print("3. Navigation")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print(object_detection())

        elif choice == "2":
            print(read_text())

        elif choice == "3":
            distance = detect_obstacles()
            print(f"Distance: {distance} cm")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()