# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/show2e
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-show2e
Version:	1.0
Release:	1
Summary:	Variants of \show for LaTeX2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/show2e
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/show2e.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This small package aims at making debugging (especially in an
interactive way) easier, by providing \show variants suited to
LaTeX2e commands (whether with optional arguments or robust)
and environments. The variant commands also display the
internal macros used by such commands, if any. The \showcs
variant helps with macros with exotic names.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/show2e/show2e.sty
%doc %{_texmfdistdir}/doc/latex/show2e/README
%doc %{_texmfdistdir}/doc/latex/show2e/show2e-fr.pdf
%doc %{_texmfdistdir}/doc/latex/show2e/show2e.pdf
#- source
%doc %{_texmfdistdir}/source/latex/show2e/show2e.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
