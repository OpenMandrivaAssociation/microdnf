# For libdnf minimal enforced dep
%global min_ldnf_ver 0.62.0
%global ldnfsomajor 2

Summary:	Lightweight implementation of DNF in C
Name:		microdnf
Version:	3.9.0
Release:	1
License:	GPLv3+
Group:		System/Configuration/Packaging
URL:		https://github.com/rpm-software-management/microdnf
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	meson >= 0.36.0
BuildRequires:	help2man
BuildRequires:	pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:	pkgconfig(libpeas-1.0) >= 1.20.0
BuildRequires:	pkgconfig(libdnf) >= %{min_ldnf_ver}
BuildRequires:	pkgconfig(smartcols)

Requires:	%{mklibname dnf %{ldnfsomajor}} >= %{min_ldnf_ver}
Requires:	gnupg
Requires:	dnf-data

%description
Micro DNF is a lightweight C implementation of DNF, designed to be used
for doing simple packaging actions when you don't need full-blown DNF and
you want the tiniest useful environments possible.

That is, you don't want any interpreter stack and you want the most
minimal environment possible so you can build up to exactly what you need.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%doc %{_mandir}/man8/microdnf.8*
