%define module	pypoppler

Summary:	Python bindings for the Poppler PDF rendering library
Name:		python-%{module}
Version:	0.12.2
Release:	0.1
Source0:	http://launchpad.net/poppler-python/trunk/development/+download/%{module}-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		https://launchpad.net/poppler-python
Provides:	%{module} = %{version}
BuildRequires:	python-devel 
BuildRequires:	python-setuptools
BuildRequires:	pygtk2.0-devel
BuildRequires:	atk-devel
BuildRequires:	libpoppler-devel
BuildRequires:	python-cairo-devel
BuildRequires:	libpoppler-glib-devel >= 0.10.5

%description
Python bindings for the Poppler PDF rendering library. It is needed to
run programs written in Python and using Poppler set.

%files
%doc README
%{py_platsitedir}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
