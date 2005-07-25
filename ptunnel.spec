Summary:	A tool for tunneling TCP connections over ICMP echo packets
Summary(pl):	Narzêdzie s³u¿±ce do tunelowania po³±czeñ TCP poprzez pakiety ICMP echo
Name:		ptunnel
Version:	0.61
Release:	0.1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.cs.uit.no/~daniels/PingTunnel/PingTunnel-%{version}.tar.gz
# Source0-md5:	ae01f6587d3915ec6642befe37035c58
Patch0:		%{name}-Makefile.patch
URL:		http://www.cs.uit.no/~daniels/PingTunnel/index.html
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ping Tunnel is a tool for reliably tunneling TCP connections over ICMP
echo request and reply packets. It is useful for evading firewalls
that, for whatever reason, prevent outgoing TCP connections, but allow
in- and outgoing ICMP packets.

%description -l pl
Ping Tunnel jest narzêdziem s³u¿±cym do niezawodnego tunelowania
po³±czeñ TCP poprzez pakiety ICMP echo request i ICMP echo reply. Ping
Tunnel jest u¿yteczny do omijania firewalli, które zabraniaj±
wychodz±cych po³±czeñ TCP, ale pozwalaj± na wchodz±ce i wychodz±ce
pakiety ICMP.

%prep
%setup -q -n PingTunnel
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README LICENSE
%attr(755,root,root) %{_bindir}/ptunnel
%{_mandir}/man8/ptunnel.8*
