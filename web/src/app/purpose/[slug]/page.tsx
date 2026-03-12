'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import StampLogo from '@/components/StampLogo';
import {
    getPurposeTag,
    getIngredientsByPurpose,
    getIngredient,
} from '@/lib/data';

const ORIGIN_COLORS: Record<string, string> = {
    '한방': '#B85C3A', '과학': '#5B7B8F', '식품': '#7B9E6B',
    '전통': '#8B7355', '아유르베다': '#D4A843',
    '현대과학': '#5B7B8F', '전통한방': '#B85C3A', '전통의학': '#8B7355', '식품유래': '#7B9E6B',
};

const EVIDENCE_MAP: Record<string, number> = {
    '매우 양호': 4, '양호': 3, '보통': 2, '제한적': 1,
};

export default function PurposePage() {
    const params = useParams();
    const slug = decodeURIComponent(params.slug as string);
    const tag = getPurposeTag(slug);
    const [menuOpen, setMenuOpen] = useState(false);

    if (!tag) {
        return (
            <div className="container detail-page" style={{ textAlign: 'center', paddingTop: '120px' }}>
                <h1 style={{ fontWeight: 300, marginBottom: 16 }}>목적을 찾을 수 없습니다</h1>
                <Link href="/" style={{ color: '#666', borderBottom: '1px solid #ccc' }}>홈으로 돌아가기</Link>
            </div>
        );
    }

    const ingredients = getIngredientsByPurpose(slug)
        .sort((a, b) => a.tier - b.tier || a.name.localeCompare(b.name));

    return (
        <>
            {/* Mobile menu */}
            <div className={`mobile-menu ${menuOpen ? 'open' : ''}`}>
                <button className="mobile-menu-close" onClick={() => setMenuOpen(false)}>×</button>
                <Link href="/" onClick={() => setMenuOpen(false)}>홈</Link>
                <Link href="/about" onClick={() => setMenuOpen(false)}>소개</Link>
            </div>

            {/* Nav */}
            <nav className="nav">
                <div className="nav-inner">
                    <Link href="/" style={{ display: 'block' }}>
                        <StampLogo size={28} />
                    </Link>
                    <button className="nav-hamburger" aria-label="메뉴" onClick={() => setMenuOpen(true)}>
                        <span /><span /><span />
                    </button>
                </div>
            </nav>

            <div className="container-wide">
                <div className="purpose-header">
                    <div className="detail-breadcrumb">
                        <Link href="/">홈</Link> / <span>{tag.display}</span>
                    </div>
                    <h1>{tag.display}</h1>
                    <p className="purpose-desc">{tag.description} — {tag.count}종</p>
                </div>

                {/* Ingredient list — editorial, no cards */}
                {ingredients.map((item) => (
                    <Link key={item.id} href={`/ingredients/${item.id}`} className="ingredient-list-item">
                        <div className="item-header">
                            <span className="item-name">{item.name}</span>
                            {item.origin_type && (
                                <>
                                    <span className="item-origin-dot" style={{ backgroundColor: ORIGIN_COLORS[item.origin_type] || '#888' }} />
                                    <span className="item-origin-label">{item.origin_type}</span>
                                </>
                            )}
                            {item.name_en && (
                                <span className="item-name-en">{item.name_en}</span>
                            )}
                        </div>
                        {item.nickname && (
                            <div className="item-nickname">{item.nickname}</div>
                        )}
                        <div className="item-desc">
                            {item.content_description || item.content_brief}
                        </div>
                        <div className="item-meta">
                            {item.evidence_level && (
                                <div className="evidence-dots">
                                    <span className="evidence-prefix">근거</span>
                                    {[0, 1, 2, 3].map((i) => (
                                        <span
                                            key={i}
                                            className={`evidence-dot ${i < (EVIDENCE_MAP[item.evidence_level || ''] || 0) ? 'filled' : 'empty'}`}
                                        />
                                    ))}
                                    <span className="evidence-label">{item.evidence_level}</span>
                                </div>
                            )}
                            <span className="tier-label">T{item.tier}</span>
                        </div>
                    </Link>
                ))}
            </div>
        </>
    );
}
