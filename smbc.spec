Summary:	Simple Samba Commander
Summary(pl):	Konsolowa przegl±darka otoczenia sieciowego
Name:		smbc
Version:	0.8.0
Release:	0.1
License:	GPL
Group:		Applications/Networking	
Source0:	http://www.air.rzeszow.pl/smbc/smbc/%{version}/%{name}-%{version}.tgz
# Source0-md5:	7014df691c55b79ed89f0bca80325e95
Source1:	%{name}.desktop
Patch0:		%{name}-ncurses.patch
URL:		http://www.air.rzeszow.pl/smbc/smbc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libsmbclient-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Samba Commander is a text mode SMBnet commander. In SMBC, you
can browse the local network or you can use the search function to
find the files. You can also download and upload files or all
directories to your computer or create remote and local directories.
SMBC has a resume function and supports UTF-8 characters.

%description -l pl
Simple Samba Commander jest prost± tekstow± przegl±dark± sieci opartej
o protokó³ SMB. Za pomoc± SMBC mo¿na przegl±daæ sieæ lokaln± lub w
poszukiwaniu konkretnego pliku wykorzystaæ funkcjê wyszukiwania.
Dostêpna jest równie¿ funkcja pobierania oraz wysy³ania plików jak i
ca³ych katalogów. SMBC zawiera funkcje automatycznego wznawiania
po³±czenia, obs³ugê wielu jêzyków wspiera równie¿ standard kodowania
znaków UTF8.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale/pl/LC_MESSAGES,%{_desktopdir}}

install src/smbc $RPM_BUILD_ROOT%{_bindir}
install src/smbc-utf-x $RPM_BUILD_ROOT%{_bindir}
install po/pl.gmo $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES/smbc.mo
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_desktopdir}/%{name}.desktop
%doc FAQ README doc/sample.smbcrc
%attr(755,root,root) %{_bindir}/*
