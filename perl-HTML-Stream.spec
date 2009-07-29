%define upstream_name	 HTML-Stream
%define upstream_version 1.60

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	HTML output stream class, and some markup utilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Output)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
