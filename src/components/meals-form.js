import React from 'react'

const MealsForm = ({ handleChange, handleSubmit, handleCancel, data }) => {
  return (
    <form onSubmit={handleSubmit}>
      <div className="field">
        <label className="label">Meal name</label>
        <div className="control">
          <input
            className="input"
            name="meal_name"
            placeholder="Meal name"
            onChange={handleChange}
            value={data.meal_name || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Meal Image</label>
        <div className="control">
          <input
            className="input"
            name="meal_image"
            placeholder="Paste the image URL here"
            onChange={handleChange}
            value={data.meal_image || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Meal price</label>
        <div className="control">
          <input
            className="input"
            name="meal_price"
            placeholder="The price of the meal"
            onChange={handleChange}
            value={data.meal_price || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Taste Rating</label>
        <div className="control">
          <input
            className="input"
            name="taste_rating"
            placeholder="write a number out of 5"
            onChange={handleChange}
            value={data.taste_rating || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Experience Rating</label>
        <div className="control">
          <input
            className="input"
            name="experience_rating"
            placeholder="write a number out of 5"
            onChange={handleChange}
            value={data.experience_rating || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Restaurant Name</label>
        <div className="control">
          <input
            className="input"
            name="restaurant_name"
            placeholder="Restaurant name"
            onChange={handleChange}
            value={data.restaurant_name || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">More info</label>
        <div className="control">
          <textarea
            className="textarea"
            placeholder="More info"
            name="more_info"
            onChange={handleChange}
            value={data.more_info || ''}
          />
        </div>
      </div>
      <div className="field">
        <label className="label">Resaurant location</label>
        <div className="control">
          <input
            className="input"
            name="restaurant_location"
            placeholder="Restaurant location"
            onChange={handleChange}
            value={data.restaurant_location || ''}
          />
        </div>
      </div>
      <button className="button is-dark">Submit</button>
      <button className="button is-dark" onClick={handleCancel}>Cancel</button>
    </form>
  )
}

export default MealsForm
