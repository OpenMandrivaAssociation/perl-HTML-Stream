%define module	HTML-Stream
%define name	perl-%{module}
%define version	1.55
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	HTML output stream class, and some markup utilities
Group:		Development/Perl
License:	GPL or Artistic
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The HTML::Stream module provides you with an object-oriented (and subclassable)
way of outputting HTML. Basically, you open up an "HTML stream" on an existing
filehandle, and then do all of your output to the HTML stream. You can intermix
HTML-stream-output and ordinary-print-output, if you like.

There's even a small built-in subclass, HTML::Stream::Latin1, which can handle
Latin-1 input right out of the box. But all in good time...

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README README.system docs examples testin
%{perl_vendorlib}/HTML
%{_mandir}/*/*

