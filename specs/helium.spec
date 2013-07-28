Name:           helium
Version:        0
Release:        0.1.20130727git%{?dist}
Summary:        A set of tools for amateur radio operators preparing high altitude balloon flights
License:        MIT
URL:            https://github.com/CodeBlock/helium
Source0:        %{name}-master.tar.gz

%description
Helium is a set of scripts/tools/libraries, specifically for the Raspberry Pi,
which assist with High Altitude Balloon launches.

%package -n python-sstvcam
Summary:        A library for preparing images (taken from the RPi camera) to send via SSTV
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       %{name} = %{version}-%{release}
Requires:       alsa-utils
Requires:       ImageMagick
Requires:       python-sh
Requires:       raspberrypi-vc-libs
Requires:       raspberrypi-vc-libs-devel
Requires:       raspberrypi-vc-utils
Requires:       raspberrypi-vc-static
Requires:       raspberrypi-vc-firmware
Requires:       robot36

%description -n python-sstvcam
This library interfaces with the Raspberry Pi's Camera Module. It handles taking
a picture, converting it to PPM, overlaying text, encoding it to Robot36, and
playing it via aplay.

%prep
%setup -q -n %{name}-master

%build
# python-sstvcam
cd python-sstvcam
%{__python} setup.py build
cd ..

%install
# Global
install -pDm 0644 config.yml.sample %{buildroot}%{_sysconfdir}/%{name}/config.yml

# python-sstvcam
cd python-sstvcam
%{__python} setup.py install --skip-build --root %{buildroot}
cd ..

%files
%doc README.md
%{_sysconfdir}/%{name}/config.yml

%files -n python-sstvcam
%{python_sitelib}/sstvcam/
%{python_sitelib}/sstvcam-*

%changelog
* Sat Jul 27 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0-0.1.20130727git
- Initial build.