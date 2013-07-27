Name:           robot36
Version:        0
Release:        0.1.20130611git%{?dist}
Summary:        Robot 36 Slow Scan TV Encoder and Decoder
License:        CC0
URL:            https://github.com/xdsopl/robot36
Source0:        %{name}-master.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  SDL-devel
Requires:       netpbm-progs
Requires:       SDL

%description
Robot 36 is one mode of many SSTV modes which transfers images using
the luminance / chrominance information of the image.

Like with other SSTV modes, the information is send using FM and needs only
800hz bandwidth for data (1500hz-2300hz) and 200hz for control (1100hz-1300hz).
Robot 36 transfers 320x240 color images in around 36 seconds, hence the name
Robot 36.

%prep
%setup -q -n %{name}-master

%build
make %{?_smp_mflags}

%install
install -pDm 0755 encode %{buildroot}%{_bindir}/%{name}-encode
install -pDm 0755 debug %{buildroot}%{_bindir}/%{name}-debug
install -pDm 0755 decode %{buildroot}%{_bindir}/%{name}-decode

%files
%doc COPYING README
%{_bindir}/%{name}-*

%changelog
* Tue Jun 11 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0-0.1.201130611git
- Initial build.
