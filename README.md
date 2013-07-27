# Helium

Helium is a set of scripts/tools/libraries, specifically for the Raspberry Pi,
which assist with High Altitude Balloon launches.

There is no programming language requirement, but all files within are
released under the MIT license.

We will try to stick with languages that are known to run decently well on the
Raspberry Pi, such as Python, Ruby, and C/C++. We'll stay off the JVM except
for any experimental scripts.

Although we'll remain as distro-agnostic as possible, we are developing these
scripts on Fedora, and they are unlikely tested elsewhere. We also include some
Fedora-specific "nice-to-haves", such as spec files for dependencies, and for
Helium itself.

# Fedora (Pidora)-specific Configuration

## Camera

Because we're using Pidora, we need to do a little bit of extra configuration
in order to use the camera module.

You can follow
[lkiesow's post](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=51&t=45329)
to enable the Pi's camera module.

In case his link goes down, I've mirrored `pidora-boot-for-camera.tar.gz` to two
additional places:

- http://static.w8upd.org/pidora-boot-for-camera.tar.gz
- http://elrod.me/pidora-boot-for-camera.tar.gz

**Don't replace `kernel.img` with the one from the .tar.gz though!**

If you do, USB ports will stop working. Something like this should work:

```bash
tar -zxvf pidora-boot-for-camera.tar.gz
mv /boot/kernel.img .
rm -rfv /boot/*
mv ./boot/* /boot/
mv ./kernel.img /boot/
```

DISCLAIMER: We are in no way responsible if this breaks you. :)

# Contents

## python-sstvcam

This library interfaces with the Raspberry Pi's
[Camera Module](http://elinux.org/Rpi_Camera_Module). It handles taking a
picture, converting it to PPM, overlaying text, encoding it to Robot36, and
playing it via aplay.

It depends on [robot36](https://github.com/xdsopl/robot36), which is
a public-domain (CC0) program by xdsopl. There is a spec file included in
`specs/`. It also depends on Python's `sh` library, `aplay`, `convert`,
and `raspistill`.

To use this library effectively, you'll want to import it in a python script,
and call the following functions:

* `take_picture()`
* `convert_picture_to_ppm()`
* `overlay_text(text, top_or_bottom)`
* `make_sstv()`
* `play_sstv()`

You'll probably want to do this in a loop (maybe with other functionality from
the other libraries mixed in), and **be sure to handle exceptions** so that your
main program doesn't ever crash, even if anything goes weird.

Depending on the exceptions you catch, you might consider falling back to
another mode (such as morse code), so that you don't lose telemetry.

## specs

These are RPM specfiles for dependencies and for Helium itself. You should be
able to cd into `specs` and run `./build-all` to build everything. We recommend
doing this on a Raspberry Pi install that is **dedicated** to building
packages, rather than shipping, e.g., `rpmbuild` on the Raspberry Pi that will
go in your balloon payload, then installing the resulting RPMs on a new install.

### Yum Repo

At some point, we'll provide a yum repo that contains all of these things.
You'll be able to add a repo file to `/etc/yum.repos.d/`, install `helium` and
instantly have all the scripts within this repo, and all dependencies,
installed. The configuration file will be in `/etc/helium/`. This is, of
course, after Helium is worth packaging.

# License

```
The MIT License (MIT)
Copyright (c) 2013 Ricky Elrod

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
