%define module	pypoppler

Summary:	Python bindings for the Poppler PDF rendering library
Name:		python-%{module}
Version:	0.10.1
Release:	%mkrel 1
Source0:	http://launchpad.net/poppler-python/trunk/development/+download/%{module}-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		https://launchpad.net/poppler-python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{module}
%py_requires -d
BuildRequires:	pygtk2.0-devel
BuildRequires:	atk-devel
BuildRequires:	libpoppler-devel
BuildRequires:	python-cairo-devel
BuildRequires:	libpoppler-glib-devel >= 0.10.5

%description
Python bindings for the Poppler PDF rendering library. It is needed to
run programs written in Python and using Poppler set.

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS
%{py_platsitedir}/poppler.la
%{py_platsitedir}/poppler.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
aclocal
autoconf

%build
%configure
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}
