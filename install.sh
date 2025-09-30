#!/data/data/com.termux/files/usr/bin/bash
echo "🔧 Installing Your UI..."

cp ~/.bashrc ~/.bashrc.bak
echo "python ~/Aosmix/aosmix.py" >> ~/.bashrc

echo "✅ UI installed. Restart Termux to launch."
