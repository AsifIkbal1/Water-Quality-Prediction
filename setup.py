# 📦 setuptools ইমপোর্ট করা হচ্ছে প্যাকেজ সেটআপের জন্য
import setuptools

# 📖 README.md ফাইলটি ওপেন করে তার কন্টেন্ট long_description হিসেবে রাখা হচ্ছে
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# 🔢 প্যাকেজের ভার্সন সেট করা হচ্ছে
__version__ = "0.0.0"

# 📁 গিটহাব রিপোজিটরির নাম
REPO_NAME = "water-quality-prediction-End-to-End-ML-Project"

# 👤 লেখকের গিটহাব ইউজারনেম
AUTHOR_USER_NAME = "asifikbal"

# 📦 সোর্স কোড যেখানে আছে
SRC_REPO = "mlProject"

# 📧 লেখকের ইমেইল
AUTHOR_EMAIL = "ikbal22205101162@diu.edu.bd"

# ⚙️ প্যাকেজের সেটআপ কনফিগারেশন
setuptools.setup(
    name=SRC_REPO,  # প্যাকেজের নাম
    version=__version__,  # ভার্সন
    author=AUTHOR_USER_NAME,  # লেখকের নাম
    author_email=AUTHOR_EMAIL,  # ইমেইল
    description="A small python package for ml app",  # সংক্ষিপ্ত বর্ণনা
    long_description=long_description,  # বিস্তারিত বর্ণনা (README থেকে নেওয়া)
    long_description_content="text/markdown",  # কন্টেন্ট টাইপ
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # 📎 গিটহাব রিপো লিংক
    project_urls={  # 🐞 বাগ রিপোর্ট লিংক
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # 📂 সোর্স ফোল্ডার নির্ধারণ
    packages=setuptools.find_packages(where="src")  # 🔍 src ফোল্ডারে থাকা সব প্যাকেজ খুঁজে বের করা
)



'''
তোমার প্রশ্নের সংক্ষিপ্ত **সারাংশ (summary)** নিচে দেওয়া হলো:

---
linkdin profile: https://www.linkedin.com/in/md-asif-ikbal/
### 🔍 **Local Package কী?**

* Local package হলো তোমার নিজের তৈরি করা একটি Python প্যাকেজ যেটা তোমার প্রোজেক্টের ভিতরেই থাকে।
* এটা এখনও PyPI তে পাবলিশ করা হয়নি।
* যেমন: `src/mylib/` টাইপের ফোল্ডার যার মধ্যে Python কোড থাকে।

---

### 🧩 **কেন Local Package ব্যবহার করো?**

* নিজের প্যাকেজ বা লাইব্রেরি তৈরি করে প্রোজেক্টে ব্যবহার করতে।
* কোড ডেভেলপ করতে করতে পরিবর্তন টেস্ট করতে (Editable mode)।

---

### 📦 **Local Package ইনস্টল করার নিয়ম:**

#### ✅ Editable Mode-এ ইনস্টল:

**requirements.txt** এ:

```
-e .
```

অথবা কমান্ড লাইনে:

```bash
pip install -e .
```

👉 এটা তোমার `setup.py` ফাইল দেখে প্যাকেজ ইনস্টল করে। ডেভেলপমেন্ট টাইমে কোড চেঞ্জ করলেই সাথে সাথে কাজ করে।

---

### 🔁 সুবিধা:

* কোড পরিবর্তনের পর নতুন করে ইনস্টল করতে হয় না
* প্যাকেজ স্ট্রাকচার ফলো করে বড় প্রোজেক্ট ম্যানেজ করা সহজ হয়

---


'''