try:
    file = open("source","w")
    file.write(input("Enter the content: "))
    file.close()
    file = open("source","r")
    text = file.read()
    dest = open("dest", "w")
    dest.write(text)
    dest.close()
    print("Done")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print(f"An undexpected error occured {e}")