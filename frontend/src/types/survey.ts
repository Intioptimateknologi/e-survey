interface Survey {
  id: number;
  created_by: string;
  title: string;
  description: string;
  json: string;
  code: string;
  progress: number;
  is_anonymous: boolean;
  status: any;
  limit: number;
  start_time: string;
  end_time: string;
  created_at: string;
  updated_at: string;
}

interface Respondent {
  id: number;
  survey: any;
  bio: any;
  location: string;
  latitude: number;
  longitude: number;
  answer: string;
  created_at: string;
  updated_at: string;
}
