'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import StampLogo from '@/components/StampLogo';

export default function Nav() {
    const [menuOpen, setMenuOpen] = useState(false);
    const pathname = usePathname();

    return (
        <>
            {/* Mobile slide-out menu */}
            <div className={`mobile-menu ${menuOpen ? 'open' : ''}`}>
                <button className="mobile-menu-close" onClick={() => setMenuOpen(false)}>×</button>
                <Link href="/" onClick={() => setMenuOpen(false)}>홈</Link>
                {pathname === '/' ? (
                    <a href="#content" onClick={() => { setMenuOpen(false); document.getElementById('content')?.scrollIntoView({ behavior: 'smooth' }); }}>
                        검색
                    </a>
                ) : (
                    <Link href="/#content" onClick={() => setMenuOpen(false)}>검색</Link>
                )}
                <Link href="/blog" onClick={() => setMenuOpen(false)}>탐구</Link>
                <Link href="/about" onClick={() => setMenuOpen(false)}>소개</Link>
            </div>

            {/* Sticky nav bar */}
            <nav className="nav" id="main-nav">
                <div className="nav-inner">
                    <Link href="/" style={{ display: 'block' }}><StampLogo size={28} /></Link>
                    <div className="nav-links-desktop">
                        <Link href="/#content" className={pathname === '/' ? 'active' : ''}>검색</Link>
                        <Link href="/blog" className={pathname.startsWith('/blog') ? 'active' : ''}>탐구</Link>
                        <Link href="/about" className={pathname === '/about' ? 'active' : ''}>소개</Link>
                    </div>
                    <button className="nav-hamburger" aria-label="메뉴" onClick={() => setMenuOpen(true)}>
                        <span /><span /><span />
                    </button>
                </div>
            </nav>
        </>
    );
}
