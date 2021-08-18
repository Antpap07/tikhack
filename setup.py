import.os
import.sys

# Versions
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`

# Remove existing downloads and binaries so we can start from scratch.
os.system("sudo apt-get remove google-chrome-stable")

# Install dependencies.
os.system("sudo apt-get update")
os.system("sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4")

# Install Chrome.
os.system("sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add")
os.system("sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list")
os.system("sudo apt-get -y update")
os.system("sudo apt-get -y install google-chrome-stable")
os.system("chmod +x tikhack.py")
