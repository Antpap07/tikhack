import.os
import.sys

# Versions
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`

# Remove existing downloads and binaries so we can start from scratch.
os.system("sudo apt-get remove google-chrome-stable")

# Install dependencies.
os.system("sudo apt-get update")
os.system("sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4")
os.system("sudo apt-get install python-pip && sudo apt-get install tor")   
os.system("pip install -U selenium")
os.system("pip install Pysocks")
os.system("pip install pyvirtualdisplay && apt-get install xvfb")

# Install Chrome.
os.system("sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add")
os.system("sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list")
os.system("sudo apt-get -y update")
os.system("sudo apt-get -y install google-chrome-stable")

# fetching drivers for the new prev release of geckodrivers
os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,OS_bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,OS_bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")
os.system("chmod +x tikhack && chmod +x setup.py")

# Give permission to run.
os.system("chmod +x tikhack.py")
