%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	DES_EDE3
Summary:	Crypt::DES_EDE3 Perl module - Triple-DES EDE implementation
Summary(pl):	Modu³ Perla Crypt::DES_EDE3 - implementacja Triple-DES EDE
Name:		perl-Crypt-DES_EDE3
Version:	0.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fde1995efa0735407a5f7c4a4c8147bc
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Crypt-DES
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%description -l pl
To jest modu³ Crypt::DES_EDE3, bêd±cy implementacj± szyfrowania i
odszyfrowywania Triple-DES EDE (encrypt-decrypt-encrypt).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/DES_EDE3.pm
%{_mandir}/man3/*
