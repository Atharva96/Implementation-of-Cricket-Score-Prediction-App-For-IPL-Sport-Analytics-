{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "parliamentary-triple",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing essential libraries\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "# Loading the dataset\n",
    "df = pd.read_csv('ipl.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "silent-thriller",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mid</th>\n",
       "      <th>date</th>\n",
       "      <th>venue</th>\n",
       "      <th>bat_team</th>\n",
       "      <th>bowl_team</th>\n",
       "      <th>batsman</th>\n",
       "      <th>bowler</th>\n",
       "      <th>runs</th>\n",
       "      <th>wickets</th>\n",
       "      <th>overs</th>\n",
       "      <th>runs_last_5</th>\n",
       "      <th>wickets_last_5</th>\n",
       "      <th>striker</th>\n",
       "      <th>non-striker</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>SC Ganguly</td>\n",
       "      <td>P Kumar</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>BB McCullum</td>\n",
       "      <td>P Kumar</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>BB McCullum</td>\n",
       "      <td>P Kumar</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>BB McCullum</td>\n",
       "      <td>P Kumar</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>BB McCullum</td>\n",
       "      <td>P Kumar</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.4</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   mid        date                  venue               bat_team  \\\n",
       "0    1  18-04-2008  M Chinnaswamy Stadium  Kolkata Knight Riders   \n",
       "1    1  18-04-2008  M Chinnaswamy Stadium  Kolkata Knight Riders   \n",
       "2    1  18-04-2008  M Chinnaswamy Stadium  Kolkata Knight Riders   \n",
       "3    1  18-04-2008  M Chinnaswamy Stadium  Kolkata Knight Riders   \n",
       "4    1  18-04-2008  M Chinnaswamy Stadium  Kolkata Knight Riders   \n",
       "\n",
       "                     bowl_team      batsman   bowler  runs  wickets  overs  \\\n",
       "0  Royal Challengers Bangalore   SC Ganguly  P Kumar     1        0    0.1   \n",
       "1  Royal Challengers Bangalore  BB McCullum  P Kumar     1        0    0.2   \n",
       "2  Royal Challengers Bangalore  BB McCullum  P Kumar     2        0    0.2   \n",
       "3  Royal Challengers Bangalore  BB McCullum  P Kumar     2        0    0.3   \n",
       "4  Royal Challengers Bangalore  BB McCullum  P Kumar     2        0    0.4   \n",
       "\n",
       "   runs_last_5  wickets_last_5  striker  non-striker  total  \n",
       "0            1               0        0            0    222  \n",
       "1            1               0        0            0    222  \n",
       "2            2               0        0            0    222  \n",
       "3            2               0        0            0    222  \n",
       "4            2               0        0            0    222  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "republican-algebra",
   "metadata": {},
   "outputs": [],
   "source": [
    "# --- Data Cleaning ---\n",
    "# Removing unwanted columns\n",
    "columns_to_remove = ['mid', 'venue', 'batsman', 'bowler', 'striker', 'non-striker']\n",
    "df.drop(labels=columns_to_remove, axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "restricted-vienna",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>bat_team</th>\n",
       "      <th>bowl_team</th>\n",
       "      <th>runs</th>\n",
       "      <th>wickets</th>\n",
       "      <th>overs</th>\n",
       "      <th>runs_last_5</th>\n",
       "      <th>wickets_last_5</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.3</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0.4</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         date               bat_team                    bowl_team  runs  \\\n",
       "0  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore     1   \n",
       "1  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore     1   \n",
       "2  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore     2   \n",
       "3  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore     2   \n",
       "4  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore     2   \n",
       "\n",
       "   wickets  overs  runs_last_5  wickets_last_5  total  \n",
       "0        0    0.1            1               0    222  \n",
       "1        0    0.2            1               0    222  \n",
       "2        0    0.2            2               0    222  \n",
       "3        0    0.3            2               0    222  \n",
       "4        0    0.4            2               0    222  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "unsigned-carol",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',\n",
       "       'Mumbai Indians', 'Deccan Chargers', 'Kings XI Punjab',\n",
       "       'Royal Challengers Bangalore', 'Delhi Daredevils',\n",
       "       'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',\n",
       "       'Rising Pune Supergiants', 'Gujarat Lions',\n",
       "       'Rising Pune Supergiant'], dtype=object)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['bat_team'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "religious-calcium",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Keeping only consistent teams\n",
    "consistent_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',\n",
    "                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',\n",
    "                    'Delhi Daredevils', 'Sunrisers Hyderabad']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "previous-plate",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[(df['bat_team'].isin(consistent_teams)) & (df['bowl_team'].isin(consistent_teams))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "numerical-dating",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Removing the first 5 overs data in every match\n",
    "df = df[df['overs']>=5.0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "hawaiian-apparel",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>bat_team</th>\n",
       "      <th>bowl_team</th>\n",
       "      <th>runs</th>\n",
       "      <th>wickets</th>\n",
       "      <th>overs</th>\n",
       "      <th>runs_last_5</th>\n",
       "      <th>wickets_last_5</th>\n",
       "      <th>total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>61</td>\n",
       "      <td>0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>59</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.2</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.3</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.4</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>18-04-2008</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.5</td>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          date               bat_team                    bowl_team  runs  \\\n",
       "32  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore    61   \n",
       "33  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore    61   \n",
       "34  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore    61   \n",
       "35  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore    61   \n",
       "36  18-04-2008  Kolkata Knight Riders  Royal Challengers Bangalore    61   \n",
       "\n",
       "    wickets  overs  runs_last_5  wickets_last_5  total  \n",
       "32        0    5.1           59               0    222  \n",
       "33        1    5.2           59               1    222  \n",
       "34        1    5.3           59               1    222  \n",
       "35        1    5.4           59               1    222  \n",
       "36        1    5.5           58               1    222  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "first-territory",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Kolkata Knight Riders' 'Chennai Super Kings' 'Rajasthan Royals'\n",
      " 'Mumbai Indians' 'Kings XI Punjab' 'Royal Challengers Bangalore'\n",
      " 'Delhi Daredevils' 'Sunrisers Hyderabad']\n",
      "['Royal Challengers Bangalore' 'Kings XI Punjab' 'Delhi Daredevils'\n",
      " 'Rajasthan Royals' 'Mumbai Indians' 'Chennai Super Kings'\n",
      " 'Kolkata Knight Riders' 'Sunrisers Hyderabad']\n"
     ]
    }
   ],
   "source": [
    "print(df['bat_team'].unique())\n",
    "print(df['bowl_team'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "australian-fisher",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Converting the column 'date' from string into datetime object\n",
    "from datetime import datetime\n",
    "df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "convertible-beaver",
   "metadata": {},
   "outputs": [],
   "source": [
    "# --- Data Preprocessing ---\n",
    "# Converting categorical features using OneHotEncoding method\n",
    "encoded_df = pd.get_dummies(data=df, columns=['bat_team', 'bowl_team'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "cardiac-letter",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>runs</th>\n",
       "      <th>wickets</th>\n",
       "      <th>overs</th>\n",
       "      <th>runs_last_5</th>\n",
       "      <th>wickets_last_5</th>\n",
       "      <th>total</th>\n",
       "      <th>bat_team_Chennai Super Kings</th>\n",
       "      <th>bat_team_Delhi Daredevils</th>\n",
       "      <th>bat_team_Kings XI Punjab</th>\n",
       "      <th>...</th>\n",
       "      <th>bat_team_Royal Challengers Bangalore</th>\n",
       "      <th>bat_team_Sunrisers Hyderabad</th>\n",
       "      <th>bowl_team_Chennai Super Kings</th>\n",
       "      <th>bowl_team_Delhi Daredevils</th>\n",
       "      <th>bowl_team_Kings XI Punjab</th>\n",
       "      <th>bowl_team_Kolkata Knight Riders</th>\n",
       "      <th>bowl_team_Mumbai Indians</th>\n",
       "      <th>bowl_team_Rajasthan Royals</th>\n",
       "      <th>bowl_team_Royal Challengers Bangalore</th>\n",
       "      <th>bowl_team_Sunrisers Hyderabad</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>59</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.2</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.3</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.4</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.5</td>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         date  runs  wickets  overs  runs_last_5  wickets_last_5  total  \\\n",
       "32 2008-04-18    61        0    5.1           59               0    222   \n",
       "33 2008-04-18    61        1    5.2           59               1    222   \n",
       "34 2008-04-18    61        1    5.3           59               1    222   \n",
       "35 2008-04-18    61        1    5.4           59               1    222   \n",
       "36 2008-04-18    61        1    5.5           58               1    222   \n",
       "\n",
       "    bat_team_Chennai Super Kings  bat_team_Delhi Daredevils  \\\n",
       "32                             0                          0   \n",
       "33                             0                          0   \n",
       "34                             0                          0   \n",
       "35                             0                          0   \n",
       "36                             0                          0   \n",
       "\n",
       "    bat_team_Kings XI Punjab  ...  bat_team_Royal Challengers Bangalore  \\\n",
       "32                         0  ...                                     0   \n",
       "33                         0  ...                                     0   \n",
       "34                         0  ...                                     0   \n",
       "35                         0  ...                                     0   \n",
       "36                         0  ...                                     0   \n",
       "\n",
       "    bat_team_Sunrisers Hyderabad  bowl_team_Chennai Super Kings  \\\n",
       "32                             0                              0   \n",
       "33                             0                              0   \n",
       "34                             0                              0   \n",
       "35                             0                              0   \n",
       "36                             0                              0   \n",
       "\n",
       "    bowl_team_Delhi Daredevils  bowl_team_Kings XI Punjab  \\\n",
       "32                           0                          0   \n",
       "33                           0                          0   \n",
       "34                           0                          0   \n",
       "35                           0                          0   \n",
       "36                           0                          0   \n",
       "\n",
       "    bowl_team_Kolkata Knight Riders  bowl_team_Mumbai Indians  \\\n",
       "32                                0                         0   \n",
       "33                                0                         0   \n",
       "34                                0                         0   \n",
       "35                                0                         0   \n",
       "36                                0                         0   \n",
       "\n",
       "    bowl_team_Rajasthan Royals  bowl_team_Royal Challengers Bangalore  \\\n",
       "32                           0                                      1   \n",
       "33                           0                                      1   \n",
       "34                           0                                      1   \n",
       "35                           0                                      1   \n",
       "36                           0                                      1   \n",
       "\n",
       "    bowl_team_Sunrisers Hyderabad  \n",
       "32                              0  \n",
       "33                              0  \n",
       "34                              0  \n",
       "35                              0  \n",
       "36                              0  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "encoded_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "particular-scout",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>runs</th>\n",
       "      <th>wickets</th>\n",
       "      <th>overs</th>\n",
       "      <th>runs_last_5</th>\n",
       "      <th>wickets_last_5</th>\n",
       "      <th>total</th>\n",
       "      <th>bat_team_Chennai Super Kings</th>\n",
       "      <th>bat_team_Delhi Daredevils</th>\n",
       "      <th>bat_team_Kings XI Punjab</th>\n",
       "      <th>...</th>\n",
       "      <th>bat_team_Royal Challengers Bangalore</th>\n",
       "      <th>bat_team_Sunrisers Hyderabad</th>\n",
       "      <th>bowl_team_Chennai Super Kings</th>\n",
       "      <th>bowl_team_Delhi Daredevils</th>\n",
       "      <th>bowl_team_Kings XI Punjab</th>\n",
       "      <th>bowl_team_Kolkata Knight Riders</th>\n",
       "      <th>bowl_team_Mumbai Indians</th>\n",
       "      <th>bowl_team_Rajasthan Royals</th>\n",
       "      <th>bowl_team_Royal Challengers Bangalore</th>\n",
       "      <th>bowl_team_Sunrisers Hyderabad</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>59</td>\n",
       "      <td>0</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.2</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.3</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.4</td>\n",
       "      <td>59</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>61</td>\n",
       "      <td>1</td>\n",
       "      <td>5.5</td>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>222</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 23 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         date  runs  wickets  overs  runs_last_5  wickets_last_5  total  \\\n",
       "32 2008-04-18    61        0    5.1           59               0    222   \n",
       "33 2008-04-18    61        1    5.2           59               1    222   \n",
       "34 2008-04-18    61        1    5.3           59               1    222   \n",
       "35 2008-04-18    61        1    5.4           59               1    222   \n",
       "36 2008-04-18    61        1    5.5           58               1    222   \n",
       "\n",
       "    bat_team_Chennai Super Kings  bat_team_Delhi Daredevils  \\\n",
       "32                             0                          0   \n",
       "33                             0                          0   \n",
       "34                             0                          0   \n",
       "35                             0                          0   \n",
       "36                             0                          0   \n",
       "\n",
       "    bat_team_Kings XI Punjab  ...  bat_team_Royal Challengers Bangalore  \\\n",
       "32                         0  ...                                     0   \n",
       "33                         0  ...                                     0   \n",
       "34                         0  ...                                     0   \n",
       "35                         0  ...                                     0   \n",
       "36                         0  ...                                     0   \n",
       "\n",
       "    bat_team_Sunrisers Hyderabad  bowl_team_Chennai Super Kings  \\\n",
       "32                             0                              0   \n",
       "33                             0                              0   \n",
       "34                             0                              0   \n",
       "35                             0                              0   \n",
       "36                             0                              0   \n",
       "\n",
       "    bowl_team_Delhi Daredevils  bowl_team_Kings XI Punjab  \\\n",
       "32                           0                          0   \n",
       "33                           0                          0   \n",
       "34                           0                          0   \n",
       "35                           0                          0   \n",
       "36                           0                          0   \n",
       "\n",
       "    bowl_team_Kolkata Knight Riders  bowl_team_Mumbai Indians  \\\n",
       "32                                0                         0   \n",
       "33                                0                         0   \n",
       "34                                0                         0   \n",
       "35                                0                         0   \n",
       "36                                0                         0   \n",
       "\n",
       "    bowl_team_Rajasthan Royals  bowl_team_Royal Challengers Bangalore  \\\n",
       "32                           0                                      1   \n",
       "33                           0                                      1   \n",
       "34                           0                                      1   \n",
       "35                           0                                      1   \n",
       "36                           0                                      1   \n",
       "\n",
       "    bowl_team_Sunrisers Hyderabad  \n",
       "32                              0  \n",
       "33                              0  \n",
       "34                              0  \n",
       "35                              0  \n",
       "36                              0  \n",
       "\n",
       "[5 rows x 23 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "encoded_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "inner-contemporary",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['date', 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5',\n",
       "       'total', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils',\n",
       "       'bat_team_Kings XI Punjab', 'bat_team_Kolkata Knight Riders',\n",
       "       'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',\n",
       "       'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',\n",
       "       'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils',\n",
       "       'bowl_team_Kings XI Punjab', 'bowl_team_Kolkata Knight Riders',\n",
       "       'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',\n",
       "       'bowl_team_Royal Challengers Bangalore',\n",
       "       'bowl_team_Sunrisers Hyderabad'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "encoded_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fancy-presentation",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rearranging the columns\n",
    "encoded_df = encoded_df[['date', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils', 'bat_team_Kings XI Punjab',\n",
    "              'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',\n",
    "              'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',\n",
    "              'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils', 'bowl_team_Kings XI Punjab',\n",
    "              'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',\n",
    "              'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',\n",
    "              'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "greater-navigator",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Splitting the data into train and test set\n",
    "X_train = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year <= 2016]\n",
    "X_test = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year >= 2017]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "documentary-filename",
   "metadata": {},
   "outputs": [],
   "source": [
    "y_train = encoded_df[encoded_df['date'].dt.year <= 2016]['total'].values\n",
    "y_test = encoded_df[encoded_df['date'].dt.year >= 2017]['total'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "lined-melissa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Removing the 'date' column\n",
    "X_train.drop(labels='date', axis=True, inplace=True)\n",
    "X_test.drop(labels='date', axis=True, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "economic-sitting",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# --- Model Building ---\n",
    "# Linear Regression Model\n",
    "from sklearn.linear_model import LinearRegression\n",
    "regressor = LinearRegression()\n",
    "regressor.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "painted-shipping",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating a pickle file for the classifier\n",
    "filename = 'first-innings-score-lr-model.pkl'\n",
    "pickle.dump(regressor, open(filename, 'wb'))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "concrete-madonna",
   "metadata": {},
   "source": [
    "Ridge Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "express-financing",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Ridge Regression\n",
    "from sklearn.linear_model import Ridge\n",
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "prescribed-truth",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_ridge.py:148: LinAlgWarning: Ill-conditioned matrix (rcond=3.27836e-22): result may not be accurate.\n",
      "  overwrite_a=True).T\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_ridge.py:148: LinAlgWarning: Ill-conditioned matrix (rcond=1.50489e-18): result may not be accurate.\n",
      "  overwrite_a=True).T\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_ridge.py:148: LinAlgWarning: Ill-conditioned matrix (rcond=1.57944e-18): result may not be accurate.\n",
      "  overwrite_a=True).T\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_ridge.py:148: LinAlgWarning: Ill-conditioned matrix (rcond=1.54481e-18): result may not be accurate.\n",
      "  overwrite_a=True).T\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_ridge.py:148: LinAlgWarning: Ill-conditioned matrix (rcond=1.5532e-18): result may not be accurate.\n",
      "  overwrite_a=True).T\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_ridge.py:148: LinAlgWarning: Ill-conditioned matrix (rcond=1.54515e-18): result may not be accurate.\n",
      "  overwrite_a=True).T\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "GridSearchCV(cv=5, estimator=Ridge(),\n",
       "             param_grid={'alpha': [1e-15, 1e-10, 1e-08, 0.001, 0.01, 1, 5, 10,\n",
       "                                   20, 30, 35, 40]},\n",
       "             scoring='neg_mean_squared_error')"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ridge=Ridge()\n",
    "parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40]}\n",
    "ridge_regressor=GridSearchCV(ridge,parameters,scoring='neg_mean_squared_error',cv=5)\n",
    "ridge_regressor.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "comic-cancer",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'alpha': 40}\n",
      "-328.4152792487922\n"
     ]
    }
   ],
   "source": [
    "print(ridge_regressor.best_params_)\n",
    "print(ridge_regressor.best_score_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "naughty-ecuador",
   "metadata": {},
   "outputs": [],
   "source": [
    "prediction=ridge_regressor.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ready-makeup",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\seaborn\\distributions.py:2557: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Density'>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "sns.distplot(y_test-prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "vulnerable-sustainability",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 12.117294527005031\n",
      "MSE: 251.03172964112676\n",
      "RMSE: 15.843980864704639\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "import numpy as np\n",
    "print('MAE:', metrics.mean_absolute_error(y_test, prediction))\n",
    "print('MSE:', metrics.mean_squared_error(y_test, prediction))\n",
    "print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "skilled-worship",
   "metadata": {},
   "source": [
    "Lasso Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "polish-fourth",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import Lasso\n",
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "interpreted-sixth",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 4282396.494295021, tolerance: 2529.9556965945617\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 4459696.004239025, tolerance: 2547.0380710286645\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 4650637.090059386, tolerance: 2667.8126904366454\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 4369586.522085682, tolerance: 2712.3488913976694\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 4588150.204673531, tolerance: 2646.143766019288\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 589202.655257564, tolerance: 2529.9556965945617\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 482836.2293441212, tolerance: 2547.0380710286645\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 253600.03883395065, tolerance: 2667.8126904366454\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 273552.6420925902, tolerance: 2712.3488913976694\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 328231.2332050791, tolerance: 2646.143766019288\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 589202.6379346913, tolerance: 2529.9556965945617\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 482835.8355714511, tolerance: 2547.0380710286645\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 253599.45482041314, tolerance: 2667.8126904366454\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 273552.75546038523, tolerance: 2712.3488913976694\n",
      "  positive)\n",
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\sklearn\\linear_model\\_coordinate_descent.py:532: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations. Duality gap: 328228.17534069344, tolerance: 2646.143766019288\n",
      "  positive)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'alpha': 1}\n",
      "-320.8263789858526\n"
     ]
    }
   ],
   "source": [
    "lasso=Lasso()\n",
    "parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40]}\n",
    "lasso_regressor=GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)\n",
    "\n",
    "lasso_regressor.fit(X_train,y_train)\n",
    "print(lasso_regressor.best_params_)\n",
    "print(lasso_regressor.best_score_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "younger-strengthening",
   "metadata": {},
   "outputs": [],
   "source": [
    "prediction=lasso_regressor.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "alien-joshua",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\atharva pathak\\anaconda3\\envs\\ipl\\lib\\site-packages\\seaborn\\distributions.py:2557: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Density'>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "sns.distplot(y_test-prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "silver-nitrogen",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 12.214053814850246\n",
      "MSE: 262.37973664007154\n",
      "RMSE: 16.198139912967523\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "import numpy as np\n",
    "print('MAE:', metrics.mean_absolute_error(y_test, prediction))\n",
    "print('MSE:', metrics.mean_squared_error(y_test, prediction))\n",
    "print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "photographic-photographer",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
