import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';

export interface BlogPost {
    slug: string;
    title: string;
    date: string;
    category: string;
    tags: string[];
    summary: string;
    thumbnail?: string;
    keywords?: string;
    content: string;         // raw markdown
    contentHtml: string;     // rendered HTML
    readingTime: number;     // estimated minutes
    relatedIngredients?: { id: string; name: string }[];
}

const BLOG_DIR = path.join(process.cwd(), '..', 'content', 'blog');

function estimateReadingTime(text: string): number {
    // Korean reading speed ~500 chars/min (vs ~200 words/min English)
    const charCount = text.replace(/[#*\-\[\]()!]/g, '').length;
    return Math.max(1, Math.ceil(charCount / 500));
}

export function getAllPosts(): BlogPost[] {
    if (!fs.existsSync(BLOG_DIR)) return [];

    const files = fs.readdirSync(BLOG_DIR).filter(f => f.endsWith('.md'));

    const posts = files.map(filename => {
        const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
        const filePath = path.join(BLOG_DIR, filename);
        const fileContent = fs.readFileSync(filePath, 'utf-8');
        const { data, content } = matter(fileContent);

        return {
            slug,
            title: data.title || '',
            date: data.date || '',
            category: data.category || '일상 건강 상식',
            tags: data.tags || [],
            summary: data.summary || '',
            thumbnail: data.thumbnail || '',
            keywords: data.keywords || '',
            content,
            contentHtml: marked(content) as string,
            readingTime: estimateReadingTime(content),
            relatedIngredients: data.relatedIngredients || [],
        } as BlogPost;
    });

    // Sort newest first
    return posts.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}

export function getPost(slug: string): BlogPost | null {
    const posts = getAllPosts();
    return posts.find(p => p.slug === slug) || null;
}

export function getPostSlugs(): string[] {
    if (!fs.existsSync(BLOG_DIR)) return [];
    return fs.readdirSync(BLOG_DIR)
        .filter(f => f.endsWith('.md'))
        .map(f => f.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, ''));
}
