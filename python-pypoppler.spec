%define module	pypoppler

Summary:	Python bindings for the Poppler PDF rendering library
Name:		python-%{module}
Version:	0.12.1
Release:	8
Source0:	http://launchpad.net/poppler-python/trunk/development/+download/%{module}-%{version}.tar.gz
Patch0:		pypoppler-0.12.1-poppler-0.16.0.patch
Patch1:		pypoppler-0.12.1-link.patch
Patch2:		pypoppler-0.12.1-poppler-0.18.0-minimal-fix.patch
Patch3:		pypoppler-0.12.1-resource_leaks.patch
License:	GPLv2+
Group:		Development/Python
Url:		https://launchpad.net/poppler-python
Provides:	%{module} = %{version}
BuildRequires:	python-devel 
BuildRequires:	pygtk2.0-devel
BuildRequires:	atk-devel
BuildRequires:	libpoppler-devel
BuildRequires:	python-cairo-devel
BuildRequires:	libpoppler-glib-devel >= 0.10.5

%description
Python bindings for the Poppler PDF rendering library. It is needed to
run programs written in Python and using Poppler set.

%files
%doc AUTHORS ChangeLog COPYING NEWS
%{py_platsitedir}/poppler.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}


%changelog
* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 0.12.1-4mdv2011.0
+ Revision: 626178
- fix build with latest poppler 0.16.0
- rebuild for new poppler

* Thu Nov 04 2010 Luc Menut <lmenut@mandriva.org> 0.12.1-3mdv2011.0
+ Revision: 593043
- rebuild for python 2.7
- drop %%py_requires macro

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 0.12.1-2mdv2011.0
+ Revision: 566259
- rebuild for new poppler

* Tue Sep 29 2009 Götz Waschk <waschk@mandriva.org> 0.12.1-1mdv2010.0
+ Revision: 450881
- update to new version 0.12.1

* Sun Sep 27 2009 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2010.0
+ Revision: 449730
- update to new version 0.12.0

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.1-1mdv2010.0
+ Revision: 444921
- update to new version 0.10.1

* Sun Aug 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1mdv2010.0
+ Revision: 422562
- change layout

  + Luc Menut <lmenut@mandriva.org>
    - import python-pypoppler


* Sat Aug 22 2009 Luc Menut <lmenut@mandriva.org> 0.10.0-1mdv2010.0
- initial Mandriva package (based on Fedora's SPEC)