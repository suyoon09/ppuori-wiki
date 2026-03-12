'use client';

import { useState, useMemo } from 'react';
import Link from 'next/link';
import StampLogo from '@/components/StampLogo';
import FlowLines from '@/components/FlowLines';
import Nav from '@/components/Nav';
import { getAllIngredients } from '@/lib/data';

const PURPOSE_OPTIONS = [
  '면역', '장건강', '노화방지', '피부', '혈압-혈당', '만성피로',
  '뼈-관절', '다이어트', '스트레스', '운동', '수면', '갱년기',
  '콜레스테롤', '간건강', '성기능', '학습-수험생', '눈건강',
  '탈모', '구강', '임산부', '숙취', '어린이성장',
];
const BODYPART_OPTIONS = [
  '전신', '장', '뇌', '심장·혈관', '피부', '뼈·관절',
  '간', '근육', '눈', '모발', '구강', '위',
];
const ORIGIN_OPTIONS = ['현대과학', '전통한방', '전통의학', '식품유래', '아유르베다'];
const ORIGIN_COLORS: Record<string, string> = {
  '한방': '#B85C3A', '과학': '#5B7B8F', '식품': '#7B9E6B',
  '전통': '#8B7355', '아유르베다': '#D4A843',
  '현대과학': '#5B7B8F', '전통한방': '#B85C3A', '전통의학': '#8B7355', '식품유래': '#7B9E6B',
};
const EVIDENCE_MAP: Record<string, number> = { '매우 양호': 4, '양호': 3, '보통': 2, '제한적': 1 };
const PER_PAGE = 20;

export default function HomePage() {
  const allIngredients = getAllIngredients();
  const [searchQuery, setSearchQuery] = useState('');
  const [filterPurpose, setFilterPurpose] = useState('');
  const [filterBody, setFilterBody] = useState('');
  const [filterOrigin, setFilterOrigin] = useState('');
  const [showFilters, setShowFilters] = useState(false);
  const [page, setPage] = useState(1);

  const scrollToContent = () => {
    document.getElementById('content')?.scrollIntoView({ behavior: 'smooth' });
  };

  const hasActiveFilters = filterPurpose || filterBody || filterOrigin;
  const isSearching = searchQuery.trim().length >= 2;

  const allFiltered = useMemo(() => {
    let items = allIngredients;
    if (isSearching) {
      const q = searchQuery.toLowerCase();
      items = items.filter((item) =>
        item.name.toLowerCase().includes(q) ||
        (item.name_en && item.name_en.toLowerCase().includes(q)) ||
        (item.nickname && item.nickname.includes(q)) ||
        (item.aliases && item.aliases.some((a: string) => a.toLowerCase().includes(q)))
      );
    }
    if (filterPurpose) items = items.filter((item) => item.tags_purpose?.includes(filterPurpose));
    if (filterBody) items = items.filter((item) => item.tags_bodypart?.includes(filterBody));
    if (filterOrigin) items = items.filter((item) => item.origin_type === filterOrigin);
    return items.sort((a, b) => a.tier - b.tier || a.name.localeCompare(b.name));
  }, [searchQuery, filterPurpose, filterBody, filterOrigin, allIngredients, isSearching]);

  const totalPages = Math.ceil(allFiltered.length / PER_PAGE);
  const pageItems = allFiltered.slice((page - 1) * PER_PAGE, page * PER_PAGE);

  // Reset page when filters change
  const updateFilter = (setter: (v: string) => void, v: string) => { setter(v); setPage(1); };
  const clearFilters = () => { setFilterPurpose(''); setFilterBody(''); setFilterOrigin(''); setSearchQuery(''); setPage(1); };

  return (
    <>
      <section className="hero">
        <div className="hero-bg"><FlowLines /></div>
        <div className="hero-stamp"><StampLogo size={44} /></div>
        <p className="hero-tagline">우리가 먹는 모든 것에는<br />기원이 있습니다</p>
        <p className="hero-sub">건강기능식품 원료 사전</p>
        <button className="hero-cta" onClick={scrollToContent}>검색<span className="arrow">↓</span></button>
      </section>

      <Nav />

      <div id="content" style={{ scrollMarginTop: '80px' }}>
        <div className="container-wide">
          <div className="content-panel" style={{ paddingBottom: '24px' }}>
            <div className="search-filter-bar">
              <input className="search-input" type="text" placeholder="원료명을 입력하세요" aria-label="원료 검색"
                value={searchQuery} onChange={(e) => { setSearchQuery(e.target.value); setPage(1); }} />
              <button className="filter-toggle-btn" onClick={() => setShowFilters(!showFilters)}>
                {showFilters ? '필터 닫기' : '상세 필터'}
              </button>
            </div>
            {showFilters && (
              <div className="filter-dropdowns">
                <div className="filter-group">
                  <label>목적</label>
                  <select value={filterPurpose} onChange={(e) => updateFilter(setFilterPurpose, e.target.value)}>
                    <option value="">전체</option>
                    {PURPOSE_OPTIONS.map((p) => <option key={p} value={p}>{p}</option>)}
                  </select>
                </div>
                <div className="filter-group">
                  <label>신체부위</label>
                  <select value={filterBody} onChange={(e) => updateFilter(setFilterBody, e.target.value)}>
                    <option value="">전체</option>
                    {BODYPART_OPTIONS.map((b) => <option key={b} value={b}>{b}</option>)}
                  </select>
                </div>
                <div className="filter-group">
                  <label>기원</label>
                  <select value={filterOrigin} onChange={(e) => updateFilter(setFilterOrigin, e.target.value)}>
                    <option value="">전체</option>
                    {ORIGIN_OPTIONS.map((o) => <option key={o} value={o}>{o}</option>)}
                  </select>
                </div>
                {hasActiveFilters && <button className="filter-clear-btn" onClick={clearFilters}>초기화</button>}
              </div>
            )}
          </div>

          <div className="content-panel" style={{ marginTop: '2px' }}>
            <div className="section-title">
              {isSearching || hasActiveFilters
                ? `검색 결과 — ${allFiltered.length}건`
                : '전체 원료'}
            </div>
            {pageItems.length === 0 && (
              <div style={{ textAlign: 'center', padding: '48px 24px', color: '#999' }}>
                <p>해당 조건에 맞는 원료를 찾을 수 없습니다.</p>
                <button onClick={clearFilters} style={{ marginTop: 12, color: '#555', textDecoration: 'underline', background: 'none', border: 'none', cursor: 'pointer' }}>필터 초기화</button>
              </div>
            )}
            {pageItems.map((item) => (
              <Link key={item.id} href={`/ingredients/${item.id}`} className="ingredient-list-item">
                <div className="item-header">
                  <span className="item-name">{item.name}</span>
                  {item.origin_type && (
                    <>
                      <span className="item-origin-dot" style={{ backgroundColor: ORIGIN_COLORS[item.origin_type] || '#888' }} />
                      <span className="item-origin-label">{item.origin_type}</span>
                    </>
                  )}
                  {item.name_en && <span className="item-name-en">{item.name_en}</span>}
                </div>
                {item.nickname && <div className="item-nickname">{item.nickname}</div>}
                <div className="item-desc">
                  {(item.content_description || item.content_brief || '').slice(0, 120)}
                  {(item.content_description || '').length > 120 ? '…' : ''}
                </div>
                <div className="item-meta">
                  {item.evidence_level && <EvidenceDots level={item.evidence_level} />}
                  <span className="tier-label">T{item.tier}</span>
                </div>
              </Link>
            ))}

            {/* Pagination */}
            {totalPages > 1 && (
              <div className="pagination">
                <button disabled={page <= 1} onClick={() => setPage(page - 1)}>← 이전</button>
                <span className="pagination-info">{page} / {totalPages}</span>
                <button disabled={page >= totalPages} onClick={() => setPage(page + 1)}>다음 →</button>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}

function EvidenceDots({ level }: { level: string }) {
  const filled = EVIDENCE_MAP[level] || 0;
  return (
    <div className="evidence-dots">
      <span className="evidence-prefix">근거</span>
      {[0, 1, 2, 3].map((i) => (
        <span key={i} className={`evidence-dot ${i < filled ? 'filled' : 'empty'}`} />
      ))}
      <span className="evidence-label">{level}</span>
    </div>
  );
}
