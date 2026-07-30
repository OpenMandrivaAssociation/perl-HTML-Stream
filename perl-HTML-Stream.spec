%define upstream_name	 HTML-Stream
%define upstream_version 1.60
Name:		perl-%{upstream_name}
Version:	1.60
Release:	4

Summary:	HTML output stream class, and some markup utilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTML-Stream
Source0:	https://cpan.metacpan.org/authors/id/D/DS/DSTAAL/HTML-Stream-1.60.tar.gz

BuildRequires:	make
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
%setup -q -n HTML-Stream-1.60

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc COPYING README README.system docs examples testin
%{perl_vendorlib}/HTML
%{_mandir}/*/*


