#!/data/data/com.termux/files/usr/bin/bash
echo "🗑️ Uninstalling Your UI..."
rm -rf ~/Aosmix
sed -i '/Aosmix/d' ~/.bashrc
sed -i '/Aosmix/d' ~/.profile
sed -i '/Aosmix/d' ~/.bash_profile
echo "✅ UI uninstalled."
