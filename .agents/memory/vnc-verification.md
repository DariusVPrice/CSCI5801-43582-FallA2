---
name: VNC verification
description: Non-obvious checks for native GUI apps in this workspace's VNC environment.
---

Do not treat a running GUI workflow as proof that its window is visible in VNC or that the browser can connect. Verify the live desktop separately from the browser connection.

**Why:** This environment had multiple working X displays. The shell's default display differed from the desktop served by the managed VNC service, so the program ran successfully without appearing in VNC. The browser route could also fail while the local VNC service remained healthy.

**How to apply:** Inspect the managed VNC display at runtime rather than assuming the shell's display is correct. Verify the rendered desktop after changing the launch command. Keep the managed VNC server and its authentication boundary intact; do not install a duplicate server or expose unauthenticated VNC as a forwarding workaround.
