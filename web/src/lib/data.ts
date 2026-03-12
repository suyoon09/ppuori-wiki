import ingredientsData from '@/data/ingredients.json';
import taxonomyData from '@/data/taxonomy.json';

export interface Ingredient {
  id: string;
  name: string;
  name_en?: string;
  aliases?: string[];
  nickname?: string;
  category: string;
  subcategory?: string;
  tags_purpose?: string[];
  tags_function?: string[];
  tags_bodypart?: string[];
  tags_age?: string[];
  tags_gender?: string[];
  daily_recommended?: string;
  upper_limit?: string;
  mfds_functionality?: string;
  related_ingredients?: string[];
  tier: number;
  source_type?: string;
  content_description?: string;
  content_brief?: string;
  content_role?: string;
  safety_class?: string;
  origin_type?: string;
  origin_story?: string;
  dosage_reference?: string;
  evidence_level?: string;
  food_sources?: string;
  food_sources_table?: { food: string; amount: string }[];
  fun_fact?: string;
  references?: string[];
}

export interface PurposeTag {
  key: string;
  display: string;
  description: string;
  functions: string[];
  count: number;
}

// Cast imported data
const ingredients = ingredientsData as Ingredient[];

// === GETTERS ===

export function getAllIngredients(): Ingredient[] {
  return ingredients;
}

export function getIngredient(id: string): Ingredient | undefined {
  return ingredients.find((i) => i.id === id);
}

export function getIngredientsByTier(tier: number): Ingredient[] {
  return ingredients.filter((i) => i.tier === tier);
}

export function getIngredientsByPurpose(purposeKey: string): Ingredient[] {
  return ingredients.filter((i) =>
    i.tags_purpose?.includes(purposeKey)
  );
}

export function getIngredientsByCategory(category: string): Ingredient[] {
  return ingredients.filter((i) => i.category === category);
}

export function getAllIngredientIds(): string[] {
  return ingredients.map((i) => i.id);
}

// === TAXONOMY ===

export function getPurposeTags(): PurposeTag[] {
  const purposeMap = taxonomyData.purpose_to_function as Record<
    string,
    { display: string; description: string; functions: string[] }
  >;
  return Object.entries(purposeMap).map(([key, val]) => ({
    key,
    display: val.display,
    description: val.description,
    functions: val.functions,
    count: getIngredientsByPurpose(key).length,
  }));
}

export function getPurposeTag(key: string): PurposeTag | undefined {
  return getPurposeTags().find((t) => t.key === key);
}

export function getAllPurposeKeys(): string[] {
  return Object.keys(taxonomyData.purpose_to_function);
}

export function getAllCategories(): string[] {
  const cats = new Set(ingredients.map((i) => i.category));
  return Array.from(cats).sort();
}

export function getCategoryDisplay(category: string): string {
  const map: Record<string, string> = {
    vitamin: '비타민',
    mineral: '미네랄',
    amino_acid: '아미노산',
    fatty_acid: '지방산',
    extract: '추출물',
    probiotic: '프로바이오틱스',
    enzyme: '효소',
    protein: '단백질',
    fiber: '식이섬유',
    other_functional: '기능성 원료',
    additive: '첨가물',
  };
  return map[category] || category;
}

// === SEARCH HELPERS ===

export function getSearchableText(ingredient: Ingredient): string {
  return [
    ingredient.name,
    ingredient.name_en,
    ingredient.nickname,
    ...(ingredient.aliases || []),
    ingredient.content_description,
    ingredient.content_brief,
  ]
    .filter(Boolean)
    .join(' ');
}

// === ORIGIN TYPE ===

export type OriginType = '전통한방' | '아유르베다' | '전통의학' | '현대과학' | '식품유래';

export function getOriginColor(origin?: string): string {
  const map: Record<string, string> = {
    '전통한방': '#B85C3A',
    '아유르베다': '#D4A843',
    '전통의학': '#8B7355',
    '현대과학': '#5B7B8F',
    '식품유래': '#7B9E6B',
  };
  return map[origin || ''] || '#9E9A90';
}

export function getOriginLabel(origin?: string): string {
  const map: Record<string, string> = {
    '전통한방': '한방',
    '아유르베다': '아유르베다',
    '전통의학': '전통',
    '현대과학': '과학',
    '식품유래': '식품',
  };
  return map[origin || ''] || '';
}

// === EVIDENCE ===

export function getEvidenceOrder(level?: string): number {
  const map: Record<string, number> = {
    '매우 양호': 4,
    '양호': 3,
    '보통': 2,
    '제한적': 1,
  };
  return map[level || ''] || 0;
}
