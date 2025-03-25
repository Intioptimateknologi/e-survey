export interface UserProfile {
  id: number;
  nik: string | null;
  phone: string | null;
  is_verified: boolean;
  is_active: boolean;
  is_deleted: boolean;
  avatar: string;
  visible_password: string;
  deleted_at: string | null;
  created_at: string;
  updated_at: string;
  user: number;
  role: string | null;
}

export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  profile: UserProfile;
}
