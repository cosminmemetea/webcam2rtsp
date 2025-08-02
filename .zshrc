export PATH="/usr/local/bin/python3.11:$PATH"
export PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:$PATH"

# Switch to Java 21:
export JAVA_HOME=$(/usr/libexec/java_home -v 21)

# Ensure the JDK 21 bin/ is first on PATH:
export PATH="$JAVA_HOME/bin:$PATH"

# webcam2rstp GStreamer fix
export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
export GI_TYPELIB_PATH=/opt/homebrew/lib/girepository-1.0

