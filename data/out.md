# MVC Implementation

Prof. Prairie UNC Comp301 Fall 2024

#### We need a playlist maker with these features:

- Add songs via title, artist, and rating
- Delete songs via a button
- Adjust order manually (up and down buttons)
- Shuffle the playlist

## 1 The Model

### Song Interface

This will hold our data and our application 'state' Our playlist is a list of songs... A song has a title, artist, and rating

```
public interface Song {
    String getTitle();
    String getArtist();
    int getRating();
```
}

#### Song Implementation:

Write a class called \"SongImpl\" that implements the interface above.

### Playlist Interface

Things to keep in mind:

- Sometimes it's not crystal clear whether something should be in the controller or in the model.
- We are going to want to iterate through the songs, so our playlist interface should extend Iterable.

```
public interface Playlist extends Iterable<Song> {
    Song getSong(int index);
    void addSong(Song song);
    void removeSong(int index);
    void moveSong(int oldIndex, int newIndex);
    void shuffleSongs();
```
//Useful for shuffling int getNumSongs();

//Model is also a Subject void addObserver(PlaylistObserver observer); void removeObserver(PlaylistObserver observer);

```
public interface PlaylistObserver {
    void update(Model model);
```
#### Playlist Implementation:

Write a class called \"PlaylistImpl\" that implements the interface above. Be prepared for Observer Pattern, if we are notifying observers this does not need to be exposed (we can assign our observers to be private).

## 2 The View

Things to keep in mind:

- Creating the App means extending Application (imported from javafx.application.Application)
- You must @Override the start method
- Main method in class calls launch()
\t- Which is an existing static method in the parent class. (equivalent to calling super.launch())

public interface FXComponent { Parent render(); }

### Rendering the View:

We want to build a hierarchical structure of reusable components. Create a class called ControlPanel that implements FXComponent, and places the shuffle button in the middle. Add the class to the View

### SongView:

- 3 buttons and a Label
- Horizontally organized
- Special Characters\"
\t- \\u274C (fancy x)
\t- \\u25B2 (up arrow)
\t- \\u25BC (Down Arrow)
\t- \\u2605 (Filled in star)
\t- \\u2606 (non-filled in star)

On the next page, create a class called SongView that implements FXComponent, and renders the above specifications (worry about the stars last, or skip entirely if you want).

Write a toString method in the class you created above that creates the string we need. This method should take in no arguments and returns the string of the song title with its corresponding rating.

#### PlaylistPanel:

.

- List of SongView Components
- Should take in a Playlist to the constructor as a parameter and encapsulate the List
- Render should create a new SongView FOR EACH song in the playlist, and return it a VBox()
- Add it to the View

Write the implementation for a class called PlaylistPanel that also implements FXComponent.

#### SongPanel:

- To instantiate the Playlist we need a song
- In the app, we create a playlist and add a song to it.
- Then we add the PlaylistPanel to the Pane
- Components: Label, TextField, Label, TextField, Slider, Button

In App, create a playlist and add a song to it. Pass it to the view, and encapsulate an instance of it. Then add the PlaylistPanel to the Pane.

Write the implementation for a class called AddSongPanel and render the components from the list above.

### 3 The Controller

What functionality are we looking for with this application?

Create the Controller Interface given the actions you came up with above.

#### ControllerImpl:

MVC architecture says that Controller needs to encapsulate a reference to the model. Create a class called ControllerImpl that implements the actions of the interface you just created.

Finish the rest of the architectural scaffolding such that the window will re-render and redisplay if the model is updated. (Hint: you may need to pass something else into the View for the update function.)

### 4 Adding Events

These buttons should probably have some sort of purpose. Add an eventhandler to the add button. You will need to:

- Create a constructor and pass through the controller
- Write a lambda expression to call the functionality using the button.setOnAction() method, which called the update method which takes in an ActionEvent as a parameter

Add an eventhandler to the delete button. (Hint: keep track of the index by adding an instance variable in the constructor, revise PlaylistPanel to support the index)

Add an eventhandler to the MoveUp and MoveDown buttons.

### 5 Adding Style

Create main.css under the resources folder, and in App add a reference to your sheet that matches your file path:

scene.getStylesheets().add(\"style/main.css\");

In ControlPanel add a style class to the pane:

Pane pane = new StackPane(); pane.getStyleClass().add(\"controls-layout\");

Add something to your css file that will be immediately visible:

.controls-layout\\{ -fx-background-color:\\#ff0000; \\}

Add 10px of padding using the (-fx-padding: 10px;):

controls-layout \\{ -fx-padding: 10px; \\}

Now connect the following code to the song panel:

```
.song-layout \\{
    -fx-border-color: \\#888888;
    -fx-padding: 5px;
    -fx-spacing: 5px; \\
}
```
Add slide styling

Finish off the styling of the add panel how you want on the next page

.

