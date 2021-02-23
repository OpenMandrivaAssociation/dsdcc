%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:           dsdcc
Version:        1.9.0
Release:        1%{?dist}
Summary:        Digital Speech Decoder (DSD) rewritten as a C++ library
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/f4exb/dsdcc
#Git-Clone:     https://github.com/f4exb/dsdcc.git
Source0:	https://github.com/f4exb/dsdcc/archive/v%{version}.tar.gz
BuildRequires:  cmake

%description
DSDcc is a complete rewrite from the original DSD (Digital Speech Decoder) project.
It provides a binary executable dsdccx and a library libdsdcc.so to be used in
other programs.
It decodes DMR, dPMR, D-Star and Yaesu System Fusion (YSF) standards.

%package -n	%{libname}
Summary:        Digital Speech Decoder (DSD) rewritten as a C++ library
Group:          System/Libraries

%description -n %{libname}
DSDcc is a complete rewrite from the original DSD (Digital Speech Decoder) project.
It provides a binary executable dsdccx and a library libdsdcc.so to be used in
other programs.
It decodes DMR, dPMR, D-Star and Yaesu System Fusion (YSF) standards.

This subpackage contains the shared library files for libdsdcc.

%package -n	%{devname}
Summary:        Development files for the dsdcc library
Group:          Development/Libraries/C and C++
Provides:	%{name}-devel = %{EVRD}
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
DSDcc is a complete rewrite from the original DSD (Digital Speech Decoder) project.
It provides a binary executable dsdccx and a library libdsdcc.so to be used in
other programs.
It decodes DMR, dPMR, D-Star and Yaesu System Fusion (YSF) standards.

This subpackage contains libraries and header files for developing
applications that want to make use of libdsdcc.

%package doc
Summary:        Documentation for DSDcc

%description doc
Documentation for DSDcc

%prep
%autosetup

%build
%cmake \
  -DUSE_MBELIB=OFF \
  -Wno-dev
%make_build

%install
%make_install -C build

%files
%{_bindir}/dsdccx*

%files -n %{libname}
%{_libdir}/libdsdcc.so.%{major}*

%files -n %{devname}
%{_includedir}/dsdcc
%{_libdir}/libdsdcc.so
%{_libdir}/pkgconfig/libdsdcc.pc

%files doc
%doc *.md
