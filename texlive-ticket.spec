Name:		texlive-ticket
Version:	0.4d
Release:	1
Summary:	Make labels, visting-cards, pins with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ticket
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ticket.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ticket.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides an easy to handle interface to produce visiting cards,
labels for your files, stickers, pins and other stuff for your
office, conferences etc. All you need is a definition of your
'ticket' included in a ticket definition file and the two
commands \ticketdefault and \ticket.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ticket
%doc %{_texmfdistdir}/doc/latex/ticket

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
