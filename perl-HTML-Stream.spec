%define upstream_name	 HTML-Stream
%define upstream_version 1.60

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	HTML output stream class, and some markup utilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Output)
BuildArch:	noarch

%description
The HTML::Stream module provides you with an object-oriented (and subclassable)
way of outputting HTML. Basically, you open up an "HTML stream" on an existing
filehandle, and then do all of your output to the HTML stream. You can intermix
HTML-stream-output and ordinary-print-output, if you like.

There's even a small built-in subclass, HTML::Stream::Latin1, which can handle
Latin-1 input right out of the box. But all in good time...

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc COPYING README README.system docs examples testin
%{perl_vendorlib}/HTML
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2010.0
+ Revision: 403259
- rebuild using %%perl_convert_version

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.60-1mdv2009.0
+ Revision: 270386
- update to new version 1.60

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.59-2mdv2009.0
+ Revision: 268522
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.59-1mdv2009.0
+ Revision: 214415
- update to new version 1.59

* Fri May 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.58-1mdv2009.0
+ Revision: 213369
- new version

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.55-3mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.55-3mdv2008.0
+ Revision: 86472
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.55-2mdv2007.0
- Rebuild

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.55-1mdk
- first mdk release

